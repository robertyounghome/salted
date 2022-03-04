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
    path('category/', views.category_index, name="category_index"),
    path('category/new/', views.category_new, name='category_new'),
    path('category/<int:category_id>/', views.category_detail, name="category_detail"),
    path('<int:account_id>/edit/', views.edit, name='edit'),
    path('<int:account_id>/delete/', views.delete, name='delete'),
    path('category/<int:category_id>/delete', views.category_delete, name="category_delete")
]
