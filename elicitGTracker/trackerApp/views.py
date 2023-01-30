
from http.client import HTTPResponse
from smtplib import SMTPResponseException
from django.shortcuts import render,redirect
from .models import*
from .models import OilModel
from django.contrib import messages
# Create your views here.

def registration(request):
    
    return render(request,'trackerApp/registration.html')
def login(request):
    return render(request,'trackerApp/login.html')
def home(request):
    return render(request,'trackerApp/home.html')
def oilProducts(request):
    displayOil=OilModel.objects.all()
    return render(request,'trackerApp/oil.html',{'displayOil':displayOil})

def drugsProducts(request):
    displayDrugs=DrugsModels.objects.all()
    return render(request,'trackerApp/drugs.html',{'displayDrugs':displayDrugs})
def perfumeProducts(request):
    displayAerosal=AerosalModels.objects.all()
    
    return render(request,'trackerApp/perfume.html',{'displayAerosal':displayAerosal})
def breadProducts(request):
    
    displayBread=BreadModels.objects.all()
    
    return render(request,'trackerApp/bread.html',{'displayBread':displayBread})
def soapProducts(request):
    displaySoap=SoaplModels.objects.all()

    return render(request,'trackerApp/soap.html',{'displaySoap':displaySoap})
def upload(request):
    return render(request,'trackerApp/upload.html')

def oiluploadView(request):
    if request.method=="POST":
        productnamec=request.POST['productname']
        description1c=request.POST['description1']
        description2c=request.POST['description2']
        oilPhotoc=request.POST['filename']
        description3c=request.POST['quantity']
        oil_data=OilModel(name=productnamec,description1=description1c,description2=description2c,description3=description3c,oilPhoto=oilPhotoc)
        confirm_data = OilModel.objects.filter(name=productnamec).exists()
        if confirm_data:
            messages.success(request,"The product already exists")
            return redirect('/oil')
        else:
            oil_data.save()
            messages.success(request,'successfully saved to the')
            return redirect('/oil')
    return render(request,'trackerApp/uploadings/oilUpload.html')
    
   