
from base64 import urlsafe_b64decode
from http.client import HTTPResponse
from smtplib import SMTPResponseException
from django.shortcuts import render,redirect
from .models import*
from .models import OilModel
from django.contrib import messages
from django.contrib.auth import login as django_login
from django.shortcuts import render, get_object_or_404
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

# Photo capture
from PIL import Image
from pytesseract import pytesseract




# end library import 
# Create your views here.
#user register



# NEW LOADS INPUT

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

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
def user_login(request):
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

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out ") 
	return redirect("home")
    
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
@login_required(login_url='login')
def oilProducts(request):
   
    displayOil=OilModel.objects.all()
    return render(request,'trackerApp/oil.html',{'displayOil':displayOil})
@login_required(login_url='login')
def drugsProducts(request):
    displayDrugs=DrugsModels.objects.all()
    return render(request,'trackerApp/drugs.html',{'displayDrugs':displayDrugs})
@login_required(login_url='login')
def perfumeProducts(request):
    displayAerosal=AerosalModels.objects.all()
    
    return render(request,'trackerApp/perfume.html',{'displayAerosal':displayAerosal})
@login_required(login_url='login')
def breadProducts(request):
    
    displayBread=BreadModels.objects.all()
    
    return render(request,'trackerApp/bread.html',{'displayBread':displayBread})
@login_required(login_url='login')
def soapProducts(request):
    displaySoap=SoaplModels.objects.all()

    return render(request,'trackerApp/soap.html',{'displaySoap':displaySoap})
@login_required(login_url='login')
def upload(request):
    oilIdViewed=OilModel.objects.all()
    drugIdViewed=DrugsModels.objects.all()
    soapIdViewed=SoaplModels.objects.all()
    aerosalIdViewed=AerosalModels.objects.all()
    breadlIdViewed=BreadModels.objects.all()
    
    upload_count=OilModel.objects.count()
    return render(request,'trackerApp/upload.html',{'oilIdViewed':oilIdViewed,
                                                    'drugIdViewed':drugIdViewed,
                                                    'soapIdViewed':soapIdViewed,
                                                    'aerosalIdViewed':aerosalIdViewed,
                                                    'breadlIdViewed':breadlIdViewed,
                                                    'upload_count':upload_count,
                                                    })
    # https://djcheatsheet.github.io/sheet/reg_with_mail_confirmation.html
    # https://dev.to/yahaya_hk/password-reset-views-in-django-2gf2
    
def oiluploadView(request):
    if request.method=="POST":
        pytesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
     
        productnamec=request.POST['productname']
        description1c=request.POST['description1']
        description2c=request.POST['description2']
        oilPhotoc=request.POST['filename']
        description3c=request.POST['quantity'] 
        # img=Image.open(oilPhotoc,'r')       
        # text = pytesseract.image_to_string(img)
        # substituted_phrase = text.replace(description2c,text )
        # print(text[:-1])
        oil_data=OilModel(name=productnamec,description1=description1c,description2=description2c,description3=description3c,oilPhoto=oilPhotoc)
        # Trial
        # end trial
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
            messages.success(request,'the data submited successfsully')
            return redirect('drugsUpload.html')
    return render(request,'trackerApp/uploadings/drugsUpload.html')
def breaduploadView(request):
    return render(request,'trackerApp/uploadings/breadUpload.html')
def soapuploadView(request):
    return render(request,'trackerApp/uploadings/soapUpload.html')
def aerosaluploadView(request):
    return render(request,'trackerApp/uploadings/breadUpload.html')


def restrictedView(request):
    restricted_goods=RestrictedGModels.objects.all()
    resticted_count=RestrictedGModels.objects.count()
    return render(request,'trackerApp/uploadings/restricted.html',{'restricted_goods':restricted_goods,'resticted_count':resticted_count})

# def password_reset_request(request):
# 	if request.method == "POST":
# 		password_reset_form = PasswordResetForm(request.POST)
# 		if password_reset_form.is_valid():
# 			data = password_reset_form.cleaned_data['email']
# 			associated_users = User.objects.filter(Q(email=data))
# 			if associated_users.exists():
# 				for user in associated_users:
# 					subject = "Password Reset Requested"
# 					email_template_name = "trackerApp/accounts/password_reset_email.txt"
# 					c = {
# 					"email":user.email,
# 					'domain':'127.0.0.1:8000',
# 					'site_name': 'Website',
# 					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
# 					"user": user,
# 					'token': default_token_generator.make_token(user),
# 					'protocol': 'http',
# 					}
# 					email = render_to_string(email_template_name, c)
# 					try:
# 						send_mail(subject, email, 'isaiahmboya9@gmail.com' , [user.email], fail_silently=False)
# 					except BadHeaderError:
# 						return HttpResponse('Invalid header found.')
# 					return redirect ("/password_reset/done/")
# 	password_reset_form = PasswordResetForm()
# 	return render(request=request, template_name="trackerApp/accounts/password_reset.html", context={"password_reset_form":password_reset_form})
