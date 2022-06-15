from . import views
from django.urls import path

urlpatterns=[
    path('sign-up',views.sign,name='sign-up'),
    path('log-in',views.log,name='log-in'),

]