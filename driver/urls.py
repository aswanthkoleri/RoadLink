from django.urls import path
from . import views
app_name='driver'
urlpatterns = [
    path('', views.index,name='index'),
    path('addDriver',views.driver,name='addDriver'),
]