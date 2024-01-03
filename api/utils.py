import os

import requests
from rest_framework.exceptions import APIException

from config.settings import BASE_DIR, API_KEY
from .models import City  


def check_database_empty():
    if City.objects.exists():
        return True

    cities_list_file = os.path.join(BASE_DIR, 'cities_list.txt')
    with open(cities_list_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cities_to_create = []

    for line in lines:
        if ' — ' in line:
            parts = line.split(' — ')
            city_name = parts[0].strip()
            coordinates = parts[1].strip().split(', ')
            latitude = float(coordinates[0])
            longitude = float(coordinates[1])

            cities_to_create.append({
                'name': city_name,
                'latitude': latitude,
                'longitude': longitude
            })

    for city_data in cities_to_create:
        city = City.objects.create(**city_data)

    return False


def get_weather(latitude: float, longitude: float) -> dict:
    url = f'https://api.weather.yandex.ru/v1/informers?lat={latitude}&lon={longitude}&lang=ru_RU'
    headers = {
        "X-Yandex-API-Key": API_KEY,
    }

    response = requests.get(url, headers=headers)
    if not response.status_code == 200:
        raise APIException('Внутренняя ошибка сервера')
    data = response.json()
    return {
        'temperature': data['fact']['temp'],
        'wind_speed': data['fact']['wind_speed'],
        'pressure': data['fact']['pressure_mm']
    }

