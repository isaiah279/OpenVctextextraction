
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
                send_mail( subject,message,email_from,  recipient_list=[recipient],)
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
    trackingProgress=TrackingInProgress.objects.all()
    displayOil_Count=OilModel.objects.all().count()
    displayBread_count=BreadModels.objects.all().count()
    displayAerosal_count=AerosalModels.objects.all().count()
    displayDrugs_count=DrugsModels.objects.all().count()
    print(displayBread_count)
    uploaded_senarios=displayOil_Count+displayBread_count+displayAerosal_count+displayDrugs_count
    return render(request,'trackerApp/home.html',{'displayOil_Count':displayOil_Count,
                                                  'displayBread_count':displayBread_count,
                                                   'displayAerosal_count':displayAerosal_count,
                                                   'displayDrugs_count':displayDrugs_count,
                                                   'uploaded_senarios':uploaded_senarios,
                                                   'trackingProgress':trackingProgress
                                                  })
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
    displayOilConting=OilModel.objects.all().count()
    return render(request,'trackerApp/oil.html',{'displayOil':displayOil,'displayOilConting':displayOilConting})
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
    displaySoap_count=SoaplModels.objects.all().count()
    return render(request,'trackerApp/soap.html',{'displaySoap':displaySoap,'displaySoap_count':displaySoap_count})
@login_required(login_url='login')
def upload(request):
    oilIdViewed=OilModel.objects.all()
    drugIdViewed=DrugsModels.objects.all()
    soapIdViewed=SoaplModels.objects.all()
    aerosalIdViewed=AerosalModels.objects.all()
    breadlIdViewed=BreadModels.objects.all()
    
    # counts
    
    
    
    
    
    return render(request,'trackerApp/upload.html',{'oilIdViewed':oilIdViewed,
                                                    'drugIdViewed':drugIdViewed,
                                                    'soapIdViewed':soapIdViewed,
                                                    'aerosalIdViewed':aerosalIdViewed,
                                                    'breadlIdViewed':breadlIdViewed,        
                                                    })
    # https://djcheatsheet.github.io/sheet/reg_with_mail_confirmation.html
    # https://dev.to/yahaya_hk/password-reset-views-in-django-2gf2

def oiluploadView(request):
    if request.method=="POST":
        # pytesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        productnamec=request.POST['productname']
        description1c=request.POST['description1']
        description2c=request.POST['description2']
        oilPhotoc=request.POST['filename']
        # uploadimage =request.FILES['filename']
        # print(type(pytesseract.image_to_string(Image.open(oilPhotoc))))
        description3c=request.POST['quantity'] 
        
        
        # fs=FileSystemStorage()
        # filename=fs.save(oilPhotoc.filename,oilPhotoc)
        
        # ulpoaded_file_path=os.path.join(settings.MEDIA_ROOT, filename)
        # text=pytesseract.image_to_string(ulpoaded_file_path)
        # print(text)
        # img=Image.open(oilPhotoc)       
        # text = pytesseract.image_to_string(img)
        # print(f"Texts are here {text}")
        # substituted_phrase = text.replace(description2c,text )
        # print(text[:-1])
       
        
        oil_data=OilModel(name=productnamec,description1=description1c,description2=description2c,description3=description3c,oilPhoto=oilPhotoc)
        # Trial
        # end trial
        messages_listed=[productnamec,description1c,description2c]
        email_from= request.user.email
        
        confirm_data = OilModel.objects.filter(name=productnamec).exists()
        if confirm_data:
            messages.success(request,"The product not advaisable for use")
            subject="REPORTED NICE CASE from"
            # send email to admin
           
            recipient_Admin='isaiahmboya9@gmail.com'
            message="Product Name :" + productnamec +"\n\n\n" + "DESCRIPTIONS:" +"\n"*3 +"1)." + description1c +"\n"*2 + "2)."+ description2c + "\n"*4 + "From :" + email_from
            send_mail( subject,message,email_from,recipient_list=[recipient_Admin])
            settings.EMAIL_COUNT+=1
            ReportedCases=settings.EMAIL_COUNT
            # Still have
            ReportedCases={'ReportedCases':ReportedCases}
            return redirect('/oil')
        else:
            oilPhotoc=request.POST['filename']
            
            # print(type(pytesseract.image_to_string(Image.open(oilPhotoc))))
            oil_data.save()
            
            image = oilPhotoc
            # image = image.name
            # path = settings.MEDIA_ROOT
            # pathz = path + "/image_uploaded/" + image

            text = pytesseract.image_to_string(Image.open(image))
            print(type(pytesseract.image_to_string(Image.open('image_uploaded'+oilPhotoc)))) # =====> add line
            # text = text.encode("ascii", "ignore")
            # text = text.decode()
            print(text)

            # Summary (0.1% of the original content).
            # summarized_text = summarize(text, ratio=0.1)
                # os.remove(pathz)
                
            
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
    
    return render(request,'trackerApp/uploadings/restricted.html',{'restricted_goods':restricted_goods})

# def count_files(request):
#     numberRepotedOil =OilModel.objects.count()
#     return render(request, 'home.html', {'numberRepotedOil': numberRepotedOil})
#  Document.objects.count()
def search_itemsV(request):
    if request.method=="POST":
        searched=request.POST['searched']
        product_searched=OilModel.objects.filter(name=searched)
        return render(request,'trackerApp/search_items.html',{"searched":searched,'product_searched':product_searched})
    else:
        return render(request,'trackerApp/search_items.html',{})
    
    
