
from http.client import HTTPResponse
from smtplib import SMTPResponseException
from django.shortcuts import render,redirect
from .models import*
from .models import OilModel
from django.contrib import messages
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
#user register

def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'trackerApp/registration.html'
    if request.method == 'POST':
        userEmail=request.POST['email']
        #print(f"Here is the email , {userEmail} ,printed well")
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                #sending confirmation email
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                subject='Confirmation Message'
                recipient=userEmail
                #fromEmail=settings.EMAIL_HOST_USER
                email_from ='isaiahmboya9@gmail.com'
                
                recipient=request.POST['email']
                

                
                message="You have registered Successfully registered"
                send_mail(
                    subject,
                    message,
                    email_from,
                    recipient_list=[recipient],
                )
                user.save()
               
                # Login the user
                # login( user)
                # redirect to accounts page:
                return redirect('login')

   # No post data availabe, let's just show the page.
    else:
        form=RegisterForm()
    return render(request, template, {'form': form})
#end registration
def login(request):
    if request.method=="POST":
        usernames=request.POST['username']
        passwords=request.POST['userpassword']
        user=authenticate(request,username=usernames,password=passwords)
        if user is not None:
            django_login(request,user)
            messages.success(request,f"You Logged in Successfully  in the System as @{{usernames}}")
            return redirect('home')
        else:
            messages.success(request,"There was an erro During Login try again or create account")
            #Try again</a><br> Or <small><a href="{% url 'registration' %}">Create account</a></small> 
            return render(request,'trackerApp/login.html')
            #
            #return HttpResponse('<h2 style="color:red;text-align:center;">Error, user does not exist or incorect password</h2>')
    return render(request,'trackerApp/login.html')
def logoutuser(request):
    logout(request)
    return redirect('login')
    
def home(request):
    return render(request,'trackerApp/home.html')
###############
def search_product(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('search', None)
        if query_name:
            results = OilModel.objects.filter(name__contains=query_name)
            return render(request, 'trackerApp/oil.html', {"results":results})
    return render(request, 'trackerApp/oil.html.html')
###############
def oilProducts(request):
    
    displayOil=OilModel.objects.all()
    return render(request,'trackerApp/oil.html',{'displayOil':displayOil})
def drugsProducts(request,slug):
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
def drugsuploadView(request):
    
    if request.method=="POST":
        productnamec=request.POST['productname']
        description1c=request.POST['description1']
        description2c=request.POST['description2']
        oilPhotoc=request.POST['filename']
        description3c=request.POST['quantity']
        
        drugs_data=DrugsModels(drugname=productnamec,description1=description1c,description2=description2c,description3=description3c,oilPhoto=oilPhotoc)
        confirm_data=DrugsModels.objects.filter(drugname=productnamec)
        if confirm_data:
            messages.success(request,'The data exist in the database')
            return redirect('/')
        else:
            drugs_data.save()
            messages.success(request,'the data submited successfully')
            return redirect('drugsUpload.html')
            
    return render(request,'trackerApp/uploadings/drugsUpload.html')
   
def breaduploadView(request):
    
    return render(request,'trackerApp/uploadings/breadUpload.html')
def soapuploadView(request):
    
    return render(request,'trackerApp/uploadings/soapUpload.html')
def aerosaluploadView(request):
    
    return render(request,'trackerApp/uploadings/breadUpload.html')
