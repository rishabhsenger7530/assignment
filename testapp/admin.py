from django.contrib import admin
from .models import BuildingInfo,UploadBuildingInfo,MeterData,HourlyConsumption
# Register your models here.


admin.site.register(BuildingInfo)
admin.site.register(UploadBuildingInfo)
admin.site.register(MeterData)
admin.site.register(HourlyConsumption)