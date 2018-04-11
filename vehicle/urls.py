from django.urls import path
from . import views
app_name='vehicle'
urlpatterns = [
    path('', views.index,name='index'),
    path('addVehicle',views.addVehicle,name='addVehicle'),
]