from django.contrib import admin
from django.urls import path
from P4214 import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('<int:clothes_id>/', views.clothes_detail,
        name= 'clothes_detail' ),
    path('<clothes_type>/', views.clothes_type,
        name='clothes_type'),

]


