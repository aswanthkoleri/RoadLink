from django.urls import path
from . import views
app_name='vehicle'
urlpatterns = [
    path('', views.index,name='index'),
    path('addVehicle',views.addVehicle,name='addVehicle'),
    path('vehicles',views.showVehicles,name='showVehicles'),
    path('delete/<int:id>',views.delete,name='delete'),
]