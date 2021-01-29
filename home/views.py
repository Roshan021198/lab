from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Message

def contact_message(request):
    print("helllll")
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        message_obj = Message.objects.create(name=name,email=email,subject=subject,message=message)
        message_obj.save()
    return redirect('index')

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
