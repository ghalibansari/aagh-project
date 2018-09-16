
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vhome, name='vhome')
#    path('signup', views.vsignup, name='vsignup'),
#    path('login', views.vlogin, name='vlogin'),
#    path('logout', views.vlogout, name='vlogout'),
]
