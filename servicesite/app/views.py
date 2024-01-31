from django.shortcuts import render,redirect
from .models import contact_details
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method=='POST':
        contact_details(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            message=request.POST.get('message'),
            ).save()
        messages.success(request, "Your Details submited successfully! Thank You❤️")
        return render(request,"index.html")
    return render (request,'index.html')

