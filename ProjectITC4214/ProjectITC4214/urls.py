from django.contrib import admin
from django.urls import path
from P4214 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('<int:clothes_id>/', views.clothes_detail,
name= 'clothes_detail' ),
]
