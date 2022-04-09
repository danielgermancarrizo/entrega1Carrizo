from multiprocessing import context
from re import template
from unicodedata import name
from urllib import request, response
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic import TemplateView 
from typing import Any, Dict 
from .models import Person,Book,Condition
from .forms import LibraryForm
from django.db.models import Q

class FormView(TemplateView):
    template_name = 'forms/index.html'
    
    def post(self,request):
        response = LibraryForm(request.POST)
      
        if response.is_valid:      
            print(response)
            obj_response = response.cleaned_data
            
            obj_person = Person(
                                name=obj_response.get('name'),
                                last_name = obj_response.get('last_name'),
                                birth_date = obj_response.get('birth_date'),
                                email = obj_response.get('email')
                                )
            obj_book = Book(
                                tittle=obj_response.get('tittle'),
                                edition = obj_response.get('edition'),
                                edition_date = obj_response.get('edition_date')
                                )
            obj_condition = Condition(
                                avaible = obj_response.get('avaible'),
                                status = obj_response.get('status'),
                                condition = obj_response.get('condition')
                                )
            
            obj_condition.save()
            obj_book.save()
            obj_person.save()

        context = {
            'form' : LibraryForm(),
            'elementsPerson' : Person.objects.all
            
        }
        return render(request,self.template_name, context)    
    
    def get(self, request):
        context = {
            'form' : LibraryForm(),
            "elementsPerson" : Person.objects.all            
        }
        return render(request, self.template_name, context)

class SearchView(TemplateView):
    template_name = 'forms/search.html'
    
    def post(self,request):
        context = {
            "elements" : Person.objects.filter(
                Q(name__iexact = request.POST.get('last_name')) | Q(last_name__iexact = request.POST.get('last_name'))
            )
            
        }
     
        return render(request,self.template_name, context)
    
    