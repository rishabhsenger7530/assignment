import csv
from .models import BuildingInfo,MeterData, HourlyConsumption
def save_building_info(file_path):
    a_csv_file = open(file_path, "r")
    dict_reader = csv. DictReader(a_csv_file)
    
    for data in csv. DictReader(a_csv_file):
        if data['id']:
            save_val = BuildingInfo.objects.create(
                buildingId = data['id'],
                buildingName = data['name']
            )



def save_meter_info(file_path):
    a_csv_file = open(file_path, "r")
    dict_reader = csv. DictReader(a_csv_file)
    
    for data in csv. DictReader(a_csv_file):
        if data['id']:
            BuildingInfoid = BuildingInfo.objects.get(pk=data['building_id'])
            
            save_val = MeterData.objects.create(
                meterid           = data['id'],
                buildingId   = BuildingInfoid,
                fuel         = data['fuel'],
                unit         = data['unit']
            )

      
def save_hourly_data(file_path):
    a_csv_file = open(file_path,  mode='r', encoding='utf-8-sig')
    dict_reader = csv. DictReader(a_csv_file)
    
    for data in csv. DictReader(a_csv_file):
        if data['meter_id']:
            print(data)
            meter_id = MeterData.objects.get(pk=data['meter_id'])
            
            save_val = HourlyConsumption.objects.create(
                meter_id           = meter_id,
                consumption        = data['consumption'],
                reading_date_time  = data['reading_date_time']
            )

      