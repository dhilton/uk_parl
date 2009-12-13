from django.db import models
from django.contrib.gis.db import models

class Constituencies(models.Model):
    name = models.CharField(max_length=60)
    area_code = models.CharField(max_length=3)
    descriptio = models.CharField(max_length=50)
    file_name = models.CharField(max_length=50)
    number = models.FloatField()
    number0 = models.FloatField()
    polygon_id = models.FloatField()
    unit_id = models.FloatField()
    code = models.CharField(max_length=7)
    hectares = models.FloatField()
    area = models.FloatField()
    type_code = models.CharField(max_length=2)
    descript0 = models.CharField(max_length=25)
    type_cod0 = models.CharField(max_length=3)
    descript1 = models.CharField(max_length=36)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
	verbose_name = "Constituency"
	verbose_name_plural = "Constituencies"

    def __unicode__(self):
        return self.name


