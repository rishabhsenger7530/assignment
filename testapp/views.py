from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import BuildingInfo, MeterData,UploadBuildingInfo,HourlyConsumption
from .forms import BuildingInfoForm,MeterForm
import os
from pathlib import Path
from .utils import save_building_info,save_meter_info, save_hourly_data
# Create your views here.

def home(request):
    url = '/'
    if request.method == 'GET':
        form = BuildingInfoForm()
        
        return render(request, 'upload_building.html', {'form':form,'url':url})
    try:
        form = BuildingInfoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'File is not CSV type')
                return redirect('testapp:home')
            # If file is too large
            if csv_file.multiple_chunks():
                messages.error(request, 'Uploaded file is too big (%.2f MB)' %(csv_file.size(1000*1000),))
                return redirect('testapp:home')

            # save and upload file 
            print("fgfdfgdg")
            form.save()
            # get the path of the file saved in the server
            BASE_DIR      = Path(__file__).resolve().parent.parent
            file_path     = os.path.join(BASE_DIR, "csvupload")
            # a = file_path+csv_file
            print(str(file_path)+"/"+str(csv_file),"3555")
            newfilepath = str(file_path)+"/"+str(csv_file)
            # a function to read the file contents and save details
            save_building_info(newfilepath)
           
    except Exception as e:
        
        messages.error(request, 'Unable to upload file. ' + repr(e))
    return redirect('home')



def upload_meterdata(request):
    url = '/upload-meter-data/'
    if request.method == 'GET':
        print("get request")
        form = BuildingInfoForm()
        return render(request, 'upload_building.html', {'form':form,'url':url})
    try:
        form = BuildingInfoForm(data=request.POST, files=request.FILES)
        print("Post request")
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'File is not CSV type')
                return redirect('testapp:upload-meter-data')
            # If file is too large
            if csv_file.multiple_chunks():
                messages.error(request, 'Uploaded file is too big (%.2f MB)' %(csv_file.size(1000*1000),))
                return redirect('testapp:upload-meter-data')

            # save and upload file 
           
            form.save()
            # get the path of the file saved in the server
            BASE_DIR      = Path(__file__).resolve().parent.parent
            file_path     = os.path.join(BASE_DIR, "csvupload")
            # a = file_path+csv_file
            print(str(file_path)+"/"+str(csv_file),"3555")
            newfilepath = str(file_path)+"/"+str(csv_file)
            # a function to read the file contents and save details
            save_meter_info(newfilepath)
           
    except Exception as e:
        
        messages.error(request, 'Unable to upload file. ' + repr(e))
    return redirect('upload-meter-data')



def upload_data_consumption(request):
    url = '/upload-data-consumption/'
    if request.method == 'GET':
        form = BuildingInfoForm()
        return render(request, 'upload_building.html', {'form':form,'url':url})
    if request.method=="POST":
       
        try:
            form = BuildingInfoForm(data=request.POST, files=request.FILES)
            
            if form.is_valid():
                print("97777777777777")
                csv_file = form.cleaned_data['csv_file']
                print("99999999999999")
                if not csv_file.name.endswith('.csv'):
                    messages.error(request, 'File is not CSV type')
                    return redirect('testapp:upload-data-consumption')
                # If file is too large
                # if csv_file.multiple_chunks():
                #     messages.error(request, 'Uploaded file is too big (%.2f MB)' %(csv_file.size(5000*5000),))
                #     return redirect('testapp:upload-data-consumption')

                # save and upload file 
                print("Post request108")
                form.save()
                # get the path of the file saved in the server
                BASE_DIR      = Path(__file__).resolve().parent.parent
                file_path     = os.path.join(BASE_DIR, "csvupload")
                # a = file_path+csv_file
                print(str(file_path)+"/"+str(csv_file),"3555")
                newfilepath = str(file_path)+"/"+str(csv_file)
                print("Post request117")
                # a function to read the file contents and save details
                save_hourly_data(newfilepath)
            
        except Exception as e:
            
            messages.error(request, 'Unable to upload file. ' + repr(e))
        return redirect('upload-data-consumption')


def show_all_buildings(request):
    data = BuildingInfo.objects.all()
    print(data)
    return render(request,'all_data.html',{'data':data})


def buildings_details(request,pk):
    data = MeterData.objects.filter(buildingId=pk)
    print(data)
    return render(request,'meter_details.html',{'data':data})


def all_consumption(request):
    from django.db.models import Sum
   
    queryset = HourlyConsumption.objects.values('meter_id').annotate(Sum('consumption'))
    data = []
    label = []
    count = 0
    for i in queryset:
        data.append(i['consumption__sum'])
        label.append(i['meter_id'])
  

    return render(request,'graph.html',{'data':data,'label':label})