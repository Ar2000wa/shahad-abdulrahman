from . import views
from django.urls import path

urlpatterns = [
    path('Madinah', views.Madinah, name='Madinah'),
    path('Jeddah', views.Jeddah, name='Jeddah'),
    path('Riyadh', views.Riyadh, name='Riyadh'),
]
