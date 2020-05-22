from django.db import models
from django.contrib.gis.db import models

class Pune_POI(models.Model):
    POI_ID = models.BigIntegerField(primary_key=True)
    LINK_ID = models.BigIntegerField(null=True)
    TYPE = models.CharField(max_length=255,null=True)
    POI_NAME = models.CharField(max_length=255,null=True)
    ST_NAME = models.CharField(max_length=255,null=True)
    Lat = models.DecimalField(decimal_places=10, max_digits=13,null=True)
    Lon = models.DecimalField(decimal_places=10, max_digits=13,null=True)
    geom = models.PointField(srid=4326, blank=True,null=True)

    class Meta:
        verbose_name_plural = "poi_data"

# Create your models here.
