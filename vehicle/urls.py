from django.urls import path
from . import views
app_name='vehicle'
urlpatterns = [
    path('create_vehicle', views.create_vehicle, name='create_vehicle'),
    path('viewall_vehicle',views.viewall_vehicle, name='viewall_vehicle'),
]