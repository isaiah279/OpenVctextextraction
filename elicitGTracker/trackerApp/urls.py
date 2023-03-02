from distutils.log import DEBUG
import statistics
from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name= 'home'),
    path('oil/', views.oilProducts,name='oil-Products'),
    path('drugs/', views.drugsProducts, name='drugs-Products'),
    path('aerosals/', views.perfumeProducts, name='perfume-Products'),
    path('bread/', views.breadProducts, name='bread-Products'),
    path('soap/', views.soapProducts, name='soap-Products'),

    
    path('search_items/',views.search_itemsV,name='search-items'),

    path('upload/', views.upload, name='upload'),
    
    path('oilUploading/', views.oiluploadView, name='oilUploading'),
    path('drugsUploading/', views.oiluploadView, name='drugsUploading'),
    path('breadUploading/', views.oiluploadView, name='breadUploading'),
    path('soapUploading/', views.oiluploadView, name='soapUploading'),
    path('aerosalUploading/', views.aerosaluploadView, name='aerosalUploading'),
    path('restricted/', views.restrictedView,name='restricted-name'),
    path('registration/', views.user_register, name='registration'),
    path('login/', views.user_login, name='login'),
    path("logout", views.logout_request, name= "logout"),
    #  path("password_change", views.password_change, name="password_change"),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='trackerApp/accounts/password_reset.html'),name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='trackerApp/accounts/pasrdone.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='trackerApp/accounts/pasrcomplete.html'),name='password_reset_complete'), 
   
    #path("password_reset", views.password_reset_request, name="password_reset"),
]  
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 
