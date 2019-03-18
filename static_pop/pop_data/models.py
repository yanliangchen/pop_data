from django.db import models

# Create your models here.

class City(models.Model):
    # """³ÇÊÐ±í"""
    id = models.AutoField(primary_key=True, verbose_name=u"cityID")
    city_name = models.CharField(verbose_name=u"cityName", max_length=50)

    class Meta:
        verbose_name = u"cityMessage"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.city_name


class NetWorkSpeed(models.Model):

    id = models.AutoField(primary_key=True, verbose_name=u"ID")
    speed = models.FloatField(verbose_name=u"Speed")
    city_left = models.IntegerField(verbose_name=u"cityLeft")
    city_right = models.IntegerField(verbose_name=u"cityRight")

    class Meta:
        verbose_name = u"cityMessage"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.speed)