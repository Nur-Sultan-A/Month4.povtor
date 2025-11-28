from django.urls import path
from . import views

urlpatterns = [
    path('writers/', views.writers, name='writers'),
    path('quotes/', views.quotes, name='quotes'),
    path('time/', views.system_time, name='system_time'),
]