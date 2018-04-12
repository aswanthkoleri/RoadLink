from django.urls import path
from . import views
app_name='repair'
urlpatterns = [
    path('', views.index,name='index'),
    path('issues',views.issues,name='issues'),
    path('update/<int:id>',views.update,name='update'),
    path('repair',views.repair,name='repair')
]