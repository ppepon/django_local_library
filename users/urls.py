from django.conf.urls import url
from django.urls import path
from users import views



urlpatterns = [
    path('', views.login, name="Login"),
    path('register/', views.register, name="Registro"),
    path('welcome/', views.welcome),

]