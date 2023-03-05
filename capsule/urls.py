from django.urls import path
from capsule import views

urlpatterns = [
    path('', views.home, name='home'),
    path('capsule', views.getCapFromDb, name='capsule'),
    path('load', views.getCapFromSpaceX, name='load'),
    path('save', views.saveCapToDb, name='save'),
    path('details', views.details, name="details"),
]