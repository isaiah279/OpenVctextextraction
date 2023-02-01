import statistics
from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name= 'home'),
    path('oil/', views.oilProducts,name='oil-Products'),
    path('drugs/', views.drugsProducts, name='drugs-Products'),
    path('perfume/', views.perfumeProducts, name='perfume-Products'),
    path('bread/', views.breadProducts, name='bread-Products'),
    path('soap/', views.soapProducts, name='soap-Products'),


    path('uploads/', views.upload, name='upload'),
    
    path('oilUploading/', views.oiluploadView, name='oilUploading'),
    path('drugsUploading/', views.oiluploadView, name='drugsUploading'),
    path('breadUploading/', views.oiluploadView, name='breadUploading'),
    path('soapUploading/', views.oiluploadView, name='soapUploading'),
    path('aerosalUploading/', views.aerosaluploadView, name='aerosalUploading'),
    
    
    path('registration/', views.user_register, name='registration'),
 
    path('login/', views.login, name='login'),
    # path('employee/', views.employee, name='employee'),
]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 