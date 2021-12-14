from django.db import models

# Create your models here.


class BuildingInfo(models.Model):
    buildingId   = models.PositiveIntegerField(primary_key=True,unique=True)
    buildingName = models.CharField(max_length=250, null=False,blank=False)


class UploadBuildingInfo(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to='csvupload/')


class MeterData(models.Model):
    meterid      = models.PositiveIntegerField(primary_key=True,unique=True)
    buildingId   = models.ForeignKey(BuildingInfo, on_delete=models.CASCADE)
    fuel         = models.CharField(max_length=250, null=False,blank=False) 
    unit         = models.CharField(max_length=250, null=False,blank=False) 


class UploadMeterInfo(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to='csvupload/')



class HourlyConsumption(models.Model):
    
    meter_id           = models.ForeignKey(MeterData, on_delete=models.CASCADE)
    consumption        = models.FloatField(blank=False, null=False) 
    reading_date_time  = models.DateTimeField()