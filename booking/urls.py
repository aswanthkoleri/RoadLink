from django.urls import path
from . import views
app_name='booking'
urlpatterns = [
    path('', views.index,name='index'),
    path('book',views.book,name='book'),
    path('bookings',views.booking,name='bookings'),
    path('pay',views.pay,name='pay'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('changestatus/<int:id>',views.change,name='delete'),
]