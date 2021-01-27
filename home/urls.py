from django.urls import path
from . import views
urlpatterns = [



    path('', views.index,name='index'),
    path('about/',views.about,name='about'),
    path('service/<int:id>/',views.service,name='service'),
]
