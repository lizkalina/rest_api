from django.shortcuts import get_object_or_404, render

from .forms import PersonForm
from .models import Person
from .services import PersonService
import pdb

def index(request):
    api_call = PersonService()
    person_list = api_call.get_people()
    return render(request, 'index.html', {'person_list': person_list})

def detail(request, pk):
    api_call = PersonService()
    person = api_call.get_person(pk)
    return render(request, 'person/detail.html', {'person': person})


### TO DO ###
def create(request, name, favorite_city):
    api_call = PersonService()
    person = api_call.create_person(name=name,favorite_city=favorite_city)
    return render(request, 'person/detail.html', {'person': person})

def update(request, pk):
    api_call = PersonService()
    person = api_call.update_person(pk=pk,name=name,favorite_city=favorite_city)
    return render(request, 'person/detail.html', {'person': person})

def delete(request, pk):
    api_call = PersonService()
    person = api_call.delete_person(pk=pk)
    return render(request, 'person/detail.html', {'person': person})
