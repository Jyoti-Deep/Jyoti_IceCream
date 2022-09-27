
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages 

# Create your views here.

def index(request):
    context = {
        "variable1":"Jyoti is great",
        "variable2":"Jyoti Deep is great"
    }
    messages.success(request,"This is a text message")
    return render(request,'index.html',context)
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html' )
    # return HttpResponse("this is aboutpage")

def services(request):
    return render(request,'services.html')
    # return HttpResponse("This is services page")

def contact(request):
    if request.method == "POST":
        input1 = request.POST.get('input1')
        input2 = request.POST.get('input2')
        input3 = request.POST.get('input3')
        input4 = request.POST.get('input4')
        input5 = request.POST.get('input5')
        contact = Contact(input1=input1, input2=input2, input3=input3, input4=input4, input5=input5, date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent' )
    return render(request, 'contact.html', )
    # return HttpResponse("This is contact page")
