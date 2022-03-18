from tkinter import N
from unicodedata import name
from django.urls import path
from .views import  DisplayIndustry,CreateIndustry,UpdateIndustry,DeleteIndustry,DisplayServicesCategories,CreateServicesCategories,UpdateServicesCategories,DeleteServicesCategories,DisplayAllClient,CreateClient,UpdateClient,DeleteClient

urlpatterns = [
    
    
  ######### INDUSTRY URLS ########################
    
    path('industies/',DisplayIndustry.as_view(), name='industries'),
    path('industry/create/',CreateIndustry.as_view(), name='createindustry' ),
    path("industry/<int:pk>/update/", UpdateIndustry.as_view(), name='industryupdate'),
    path("Industry/<int:pk>/delete/",DeleteIndustry.as_view(), name='industrydelete'),
    
   ########### SERVICE URLS ########################
   path('services/',DisplayServicesCategories.as_view(), name='services' ),
   path('services/create',CreateServicesCategories.as_view(), name='createservices'),
   path('services/<int:pk>/update/',UpdateServicesCategories.as_view(), name='serviceupdate'),
   path('services/<int:pk>/delete', DeleteServicesCategories.as_view(), name='servicedelete'),
   
   ########## CLIENT URLS ###################
   path('',DisplayAllClient.as_view(), name='clients'),
   path('client/',CreateClient.as_view(), name='createclient'),
   path('client/<int:pk>/update/>',UpdateClient.as_view(), name='clientupdate'),
   path('client/<int:pk>/delete/>',DeleteClient.as_view(), name='clientdelete')
   
    
    
    
    
    
    
]