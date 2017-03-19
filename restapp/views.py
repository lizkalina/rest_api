from django.shortcuts import get_object_or_404, render, redirect

from .forms import PersonForm
from .models import Person
from .services import PersonService
import pdb
import json

def index(request):
    api_call = PersonService()
    person_list = api_call.get_people()
    return render(request, 'index.html', {'person_list': person_list})

def detail(request,pk):
    api_call = PersonService()
    person = api_call.get_person(pk)
    return render(request, 'person/detail.html', {'person': person})

def new(request):
    form = PersonForm()
    return render(request, 'person/form.html', {'form': form})

def edit(request,pk):
    api_call = PersonService()
    person = api_call.get_person(pk)
    form = PersonForm()
    return render(request, 'person/edit_form.html', {'form': form})

def create(request):
    person_info = json.dumps(request.POST)
    api_call = PersonService()
    person = api_call.create_person(person_info)
    return redirect('person_detail',pk=person['id'])

def update(request,pk):
    person_info = json.dumps(request.POST)
    api_call = PersonService()
    person = api_call.update_person(pk,person_info)
    return redirect('person_detail',pk=pk)

def delete(request, pk):
    api_call = PersonService()
    person = api_call.delete_person(pk=pk)
    return redirect('index')
