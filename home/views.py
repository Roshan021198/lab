from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Message

# Create your views here.
def index(request):
    return render(request,'index.html')

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

