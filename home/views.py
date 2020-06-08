from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    #return HttpResponse("this is my about page")
    return render(request,'about.html')

def contact(request):
    #return HttpResponse("this is my contact page")
    if request.method == "POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       phone_no = request.POST.get('phone_no')
       desc = request.POST.get('desc')        
       contact = Contact(name=name,email=email,phone_no=phone_no,desc=desc,date = datetime.today())
       contact.save()
    return render(request,"contact.html")
    
def services(request):
    #return HttpResponse("this is services")
    return render(request,'services.html')

def facilities(request):
    return render(request,'facilities.html')


