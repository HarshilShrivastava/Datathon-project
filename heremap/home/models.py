from django.db import models
from django.contrib.gis.db import models

class Pune_POI(models.Model):
    POI_ID = models.BigIntegerField(primary_key=True)
    LINK_ID = models.BigIntegerField()
    TYPE = models.CharField(max_length=255)
    POI_NAME = models.CharField(max_length=255)
    ST_NAME = models.CharField(max_length=255)
    Lat = models.DecimalField(decimal_places=10, max_digits=13)
    Lon = models.DecimalField(decimal_places=10, max_digits=13)
    # geom = models.PointField(srid=4326)

# Create your models here.
