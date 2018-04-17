from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="account"

urlpatterns =[
    path('signup',views.signup,name='signup'),
    path('login',views.loginView,name='login'),
    path('logout',views.logoutView,name='logout'),
    path('profile',views.profileView,name='profile'),
    path('edit',views.editView,name='edit'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)