from django.db import models
class data(models.Model):
    comment=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    User_lat=models.DecimalField(decimal_places=10, max_digits=13)
    User_lon=models.DecimalField(decimal_places=10, max_digits=13)
    POI_NAME = models.CharField(max_length=255,null=True)
    ST_NAME = models.CharField(max_length=255,null=True)
