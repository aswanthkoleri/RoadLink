from django.urls import path
from . import views
app_name='home'
urlpatterns = [
	path('404', views.notfound,name='index'),
    path('', views.index,name='index'),
]