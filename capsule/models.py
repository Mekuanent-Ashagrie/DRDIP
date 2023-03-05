from django.db import models

class capsules(models.Model):
    reuse_count = models.IntegerField()
    water_landings = models.IntegerField()
    land_landings = models.IntegerField()
    last_update = models.CharField(max_length=100,)
    serial = models.CharField(max_length=30,)
    status = models.CharField(max_length=50,)
    type =  models.CharField(max_length=50,)
    cid = models.CharField(primary_key=True, max_length=20,)

class launches(models.Model):
    id = models.AutoField(primary_key=True)
    cid = models.ForeignKey(capsules, on_delete=models.CASCADE)
    launch = models.CharField(max_length=20,)
    