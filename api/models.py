from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование', blank=False, null=False)
    last_updated = models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения', null=True)
    latitude = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Широта')
    longitude = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Долгота')
    temperature = models.IntegerField(verbose_name='Текущая температура (°C)', null=True)
    wind_speed = models.IntegerField(verbose_name='Скорость ветра (м/с)', null=True)
    pressure = models.IntegerField(verbose_name='Атмосферное давление (мм. рт.ст.)', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        db_table = 'cities'


