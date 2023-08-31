from django.urls import path
from django.urls import include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    #path('', views.index),
    #path('', TemplateView.as_view(template_name='reg/home.html'), name='home'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.Register.as_view(), name='register'),
]

