from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('contact_message/', views.contact_message,name='contact_message'),
]
