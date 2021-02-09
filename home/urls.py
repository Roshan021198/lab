from django.urls import path
from . import views
urlpatterns = [



    path('', views.index,name='index'),
    path('contact_message/', views.contact_message,name='contact_message'),
    path('about/',views.about,name='about'),
    path('service/<int:id>/',views.service,name='service'),
    path('singleblog/<int:id>/',views.singleblog,name='singleblog'),
    path('blog/',views.blog,name='blog'),
    
]
