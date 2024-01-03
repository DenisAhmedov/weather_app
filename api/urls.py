from django.urls import path

from api.views import CheckDB, GetWeather

urlpatterns = [
    path('check_db', CheckDB.as_view(), name='check-db'),
    path('weather', GetWeather.as_view(), name='get-weather')
]