from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('signup',views.signup, name = 'signup'),
    path('login',views.login_view, name = 'login'),
    path('weather-app',views.weather, name = 'weather'),
    path('weather-app/city/<int:city_id>/delete',views.delete, name = 'delete_city'),
    path('weather-app/delete_all', views.delete_all, name = 'delete_all'),
    path('weather-app/logout', views.logout_view, name = 'logout')
]