from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'builder-home'),
    path('about/', views.about, name = 'builder-about'),
]
