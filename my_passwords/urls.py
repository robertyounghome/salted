from django.contrib import admin
from django.urls import path, include
from my_passwords.views import AboutView

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:account_id>/', views.detail, name='detail'),
    path('new/', views.new, name="new"),
    path('thanks/', views.thanks, name="thanks"),
    path('about/', views.AboutView.as_view(), name="about"),
]
