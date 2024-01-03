import os
import django
import pytest

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from rest_framework.test import APIClient

from api.models import City


@pytest.fixture(autouse=True)
@pytest.mark.django_db
def add_record_in_db():
    City.objects.create(
        name='Абакан',
        latitude=53.72,
        longitude=91.43,
        temperature=15
    )
    yield

    City.objects.all().delete()


@pytest.fixture
@pytest.mark.django_db
def client():
    return APIClient()


@pytest.fixture
@pytest.mark.django_db
def valid_city():
    city = City.objects.first()
    return city

