from . import views
from django.urls import path

urlpatterns = [
    path('beauty', views.beauty, name='beauty'),
    path('fashion', views.fashion, name='fashion'),
    path('weddings', views.weddings, name='weddings'),
]