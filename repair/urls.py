from django.urls import path
from . import views
app_name='repair'
urlpatterns = [
    path('', views.index,name='index'),
    path('issues',views.issues,name='issues'),
    path('update/<int:id>',views.update,name='update'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('repair',views.repair,name='repair')
]