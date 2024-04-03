from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user, name='register'),
    path('login/', views.login, name='login'),
    path('login.html', views.login, name='login_html'),  
    path('logout/', views.logout, name='logout'),
]
