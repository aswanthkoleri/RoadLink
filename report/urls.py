from django.urls import path
from . import views

app_name='report'
urlpatterns = [
    path('mail',views.change,name='delete'),
    path('', views.index,name='index'),
]