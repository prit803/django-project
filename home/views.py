from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #for response in server

def home(request):
        context = {'page' : 'home'}
        return render(request, "home/index.html" , context)

def contact(request):
        context = {'page' : 'contact'} 
        return render(request, "home/contact.html" ,context )

def about(request):
        context = {'page' : 'about'} 
        return render(request, "home/about.html" ,context)

