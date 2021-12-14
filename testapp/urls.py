from django.urls import path, include
from testapp import views
urlpatterns = [
   path('', views.home,name ='home'),
   path('upload-meter-data/', views.upload_meterdata,name ='upload-meter-data'),
   path('upload-data-consumption/', views.upload_data_consumption,name ='upload-data-consumption'),
   path('show-all-buildings/', views.show_all_buildings,name ='show-all-buildings'),
   path('building-details/<int:pk>', views.buildings_details,name ='building-details'),
   path('all-consumption', views.all_consumption,name ='all-consumption'),
]


