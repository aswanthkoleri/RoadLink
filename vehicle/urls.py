from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='vehicle'
urlpatterns = [
    path('', views.index,name='index'),
    path('addVehicle',views.addVehicle,name='addVehicle'),
    path('vehicles',views.showVehicles,name='showVehicles'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)