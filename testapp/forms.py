from django import forms
from django.forms.widgets import FileInput
from .models import UploadBuildingInfo,UploadMeterInfo

class BuildingInfoForm(forms.ModelForm):
    class Meta:
        model = UploadBuildingInfo
        fields = ("csv_file",)
    widgets = {
            'csv_file': FileInput(attrs={'class': "form-control"})
        }



class MeterForm(forms.ModelForm):
    class Meta:
        model = UploadMeterInfo
        fields = ("csv_file",)
    widgets = {'csv_file': FileInput(attrs={'class': "form-control"})}