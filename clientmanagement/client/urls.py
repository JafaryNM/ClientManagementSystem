from tkinter import N
from unicodedata import name
from django.urls import path
from .views import  DisplayIndustry,CreateIndustry,UpdateIndustry,DeleteIndustry,DisplayServicesCategories,CreateServicesCategories,UpdateServicesCategories,DeleteServicesCategories

urlpatterns = [
    
    
  ######### INDUSTRY URLS ########################
    
    path('industies/',DisplayIndustry.as_view(), name='industries'),
    path('industry/create/',CreateIndustry.as_view(), name='createindustry' ),
    path("industry/<int:pk>/update/", UpdateIndustry.as_view(), name='industryupdate'),
    path("Industry/<int:pk>/delete/",DeleteIndustry.as_view(), name='industrydelete'),
    
   ########### SERVICE URLS ########################
   path('',DisplayServicesCategories.as_view(), name='services' ),
   path('services/create',CreateServicesCategories.as_view(), name='createservices'),
   path('services/<int:pk>/update/',UpdateServicesCategories.as_view(), name='serviceupdate'),
   path('services/<int:pk>/delete', DeleteServicesCategories.as_view(), name='servicedelete'),
   
   ########## CLIENT URLS ###################
    
    
    
    
    
    
]