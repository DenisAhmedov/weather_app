from rest_framework import serializers

from api.models import City


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('temperature', 'wind_speed', 'pressure')


