from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='forms'),
    path('contact-us/', views.contact, name='contact-form'),
    path('success/', views.message_success, name='success'),

]