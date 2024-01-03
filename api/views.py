from datetime import timedelta

from django.utils import timezone
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import City
from api.serializers import WeatherSerializer
from api.utils import check_database_empty, get_weather


class CheckDB(APIView):
    def get(self, request):
        result = check_database_empty()
        if result:
            return Response({'message': 'Database exists'})
        else:
            return Response({'message': 'Database created'}, status=status.HTTP_201_CREATED)


class GetWeather(APIView):
    def get(self, request):
        if city_name := request.GET.get('city'):
            city = get_object_or_404(City, name=city_name)
            time_difference = timezone.now() - city.last_updated
            if time_difference > timedelta(minutes=30):
                weather_data = get_weather(city.latitude, city.longitude)
                city.wind_speed = weather_data['wind_speed']
                city.temperature = weather_data['temperature']
                city.pressure = weather_data['pressure']
                city.save()
            serializer = WeatherSerializer(city)
            return Response(serializer.data)
        else:
            raise ValidationError('Bad request')

