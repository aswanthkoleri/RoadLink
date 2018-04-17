from django.urls import path
from . import views
app_name='driver'
urlpatterns = [
    path('', views.index,name='index'),
    path('addDriver',views.driver,name='addDriver'),
    path('drivers',views.drivers,name='drivers'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
]