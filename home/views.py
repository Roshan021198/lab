from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery,Team,Testimonials,ServiceProduct,Ceategory


# Create your views here.
def index(request):
    gallery=Gallery.objects.all()
    team=Team.objects.all()
    testimonials=Testimonials.objects.all()
    ceategory=Ceategory.objects.all()

    prams={
        'gallery':gallery,
        'team':team,
        'testimonials':testimonials,
        'ceategory':ceategory,
    }
    return render(request,'index.html',prams)
def about(request):
    return render(request,'about.html')
def service(request,id):
    ceategory=Ceategory.objects.all()
    ct=''
    serviceproduct=ServiceProduct.objects.filter(category_id=id)
    for rs in serviceproduct:
        ct=rs.category
    prms={
        'products':serviceproduct,
        'ct':ct
    }
    return render(request,'machine.html',prms)