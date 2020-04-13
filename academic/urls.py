from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'academic'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
