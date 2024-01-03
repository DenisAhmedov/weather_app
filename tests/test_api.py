import pytest

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.reverse import reverse

from api.utils import get_weather


@pytest.mark.django_db
def test_get_weather_view_with_valid_city(client, valid_city):
    url = reverse('get-weather')
    response = client.get(url, {'city': valid_city.name})

    assert response.status_code == status.HTTP_200_OK
    assert 'temperature' in response.data
    assert response.data['temperature'] == valid_city.temperature


@pytest.mark.django_db
def test_get_weather_view_with_invalid_city(client):
    url = reverse('get-weather')
    response = client.get(url, {'city': 'Дрезден'})

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_get_weather_view_with_bad_params(client):
    url = reverse('get-weather')
    response = client.get(url, {'town': 'Абакан'})

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_request_to_yandex_api(valid_city):
    response = get_weather(latitude=valid_city.latitude, longitude=valid_city.longitude)

    assert type(response) == dict
    assert 'temperature' in response
    assert 'wind_speed' in response
    assert 'pressure' in response
    assert type(response['temperature']) == int
    assert type(response['wind_speed']) == int
    assert type(response['pressure']) == int


@pytest.mark.django_db
def test_bad_request_to_yandex_api():
    with pytest.raises(APIException):
        get_weather(latitude=1175.00, longitude=280.7777)

