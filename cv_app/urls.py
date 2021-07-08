from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cv/<str:phone>/', views.cv, name='cv_app'),
]
