from pyexpat import model
from django.shortcuts import render

from .models import *

from django.views.generic import TemplateView, ListView, CreateView,UpdateView,DeleteView

# Create your views here.


### INDUSTRY CRUD #############

#List All Industry
class DisplayIndustry(ListView):
    model=Industry
    template_name='client/all_client.html'
    
    def get_context_data(self, **kwargs):
        context = super(DisplayIndustry, self).get_context_data(**kwargs)
        context['industries']=Industry.objects.all()
        return context
    
# Add New Industry

class CreateIndustry(CreateView):
    model=Industry
    template_name='client/form.html'
    fields='__all__'
    success_url='/'
   
   
# Update Industry

class UpdateIndustry(UpdateView):
    model=Industry
    template_name='client/form.html'
    fields='__all__'
    success_url='/'

# Delete Industry
class DeleteIndustry(DeleteView):
     model=Industry
     success_url='/'
     
     
     
############## SERVICE CATEGORY CRUD ##########

#list of all service categories

class DisplayServicesCategories(ListView):
    model=ServicesCategory
    template_name='services/all_services.html'
    
    def get_context_data(self, **kwargs):
        context = super(DisplayServicesCategories, self).get_context_data(**kwargs)
        context['services']=ServicesCategory.objects.all()
        return context


# Create New Categories
 
class CreateServicesCategories(CreateView):
    model=ServicesCategory
    template_name='services/form.html'
    fields='__all__'
    success_url='/'
    
    
# Update New Services Categories
 
class UpdateServicesCategories(UpdateView):
    model=ServicesCategory
    template_name='services/form.html'
    fields='__all__'
    success_url='/'

# Delete Services
class DeleteServicesCategories(DeleteView):
    model=ServicesCategory
    success_url='/'
    
########## CLIENT CRUD #############