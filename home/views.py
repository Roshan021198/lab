from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Message
from .models import Gallery,Team,Testimonials,ServiceProduct,Ceategory,News,TariffChart

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def contact_message(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        message_obj = Message.objects.create(name=name,email=email,subject=subject,message=message)
        message_obj.save()
    return redirect('index')




# Create your views here.
def index(request):
    gallery=Gallery.objects.all()
    team=Team.objects.all()
    testimonials=Testimonials.objects.all()
    ceategory=Ceategory.objects.all()
    news=News.objects.filter(status=True).order_by("upcoming_date")[:3]

    prams={
        'gallery':gallery,
        'team':team,
        'testimonials':testimonials,
        'ceategory':ceategory,
        'news':news
    }
    return render(request,'index.html',prams)
def about(request):
    ceategory=Ceategory.objects.all()
    prams={
      
        'ceategory':ceategory,
    }
    return render(request,'about.html',prams)
def service(request,id):
    ceategory=Ceategory.objects.all()
    ct=''
    serviceproduct=ServiceProduct.objects.filter(category_id=id)
    for rs in serviceproduct:
        ct=rs.category
    prms={
        'products':serviceproduct,
        'ct':ct,
        'ceategory':ceategory,
    }
    return render(request,'machine.html',prms)

def singleblog(request,id):
    ceategory=Ceategory.objects.all()
    news=News.objects.filter(id=id)
    prms={
        'ceategory':ceategory,
        'news':news,
    }
    return render(request,'singleblog.html',prms)
def blog(request):
    ceategory=Ceategory.objects.all()
    all_news=Paginator(News.objects.all(),6)
    page=request.GET.get('page')
    try:
        news=all_news.page(page)
    except PageNotAnInteger:
        news=all_news.page(1)
    except EmptyPage:
        news=all_news.page(all_news.num_pages)        
    prms={
        'ceategory':ceategory,
        'news':news ,
    } 
    return render(request,'blog.html',prms)    


def booking(request):
    ceategory=Ceategory.objects.all()
    tariff_obj = TariffChart.objects.all()
    return render(request,'tariff.html',{'tariffs':tariff_obj,'ceategory':ceategory})


def gallery(request):
    #tariff_obj = TariffChart.objects.all()
    gallery=Gallery.objects.all()
    ceategory=Ceategory.objects.all()
    return render(request,'gallery.html',{'gallery':gallery,'ceategory':ceategory})