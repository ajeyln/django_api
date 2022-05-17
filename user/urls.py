from django import views
from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('view', views.view, name='view'),
    path('<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
