from django.shortcuts import get_object_or_404, render, redirect

from .forms import PersonForm
from .services import PersonAPI
from api.people.models import Person

import json

def index(request):
    api = PersonAPI()
    person_list = api.get_people()
    return render(request, 'index.html', {'person_list': person_list})

def detail(request,pk):
    api = PersonAPI()
    person = api.get_person(pk)
    return render(request, 'person/detail.html', {'person': person, 'pk': pk})

def new(request):
    form = PersonForm()
    return render(request, 'person/new.html', {'form': form})

def edit(request,pk):
    api = PersonAPI()
    person = api.get_person(pk)
    form = PersonForm(person)
    return render(request, 'person/edit.html', {'form': form, 'pk': pk})

def create(request):
    person_info = json.dumps(request.POST)
    api = PersonAPI()
    person = api.create_person(person_info)
    return redirect('person_detail',pk=person['id'])

def update(request,pk):
    person_info = json.dumps(request.POST)
    api = PersonAPI()
    person = api.update_person(pk,person_info)
    return redirect('person_detail',pk=pk)

def delete(request, pk):
    api = PersonAPI()
    person = api.delete_person(pk=pk)
    return redirect('index')
