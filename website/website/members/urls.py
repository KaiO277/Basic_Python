from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),   
    path('setting/', views.settings, name='setting'),
    path('upload/', views.upload, name='upload'),
    path('signup/', views.signup, name='signup'),  
    path('logout/', views.logout, name='logout'),   
]