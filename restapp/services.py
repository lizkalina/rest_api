import requests
from helpers import _url
import pdb

class PersonService:

    def __init__(self,pk=None,name=None,favorite_city=None):
        self.pk = pk
        self.name = name
        self.favorite_city = favorite_city

    def get_people(self):
        return requests.get(_url('/people/'))

    def get_person(self):
        return requests.get(_url('/people/{}/'.format(self.pk)))

    def create_person(self):
        return requests.post(_url('/people/'), json={
            'name': self.name,
            'favorite_city': self.favorite_city,
            })

    def delete_person(self):
        return requests.delete(_url('/people/{}/'.format(self.pk)))

    def update_person(self):
        url = _url('/people/{}/'.format(self.pk))
        return requests.put(url, json={
            'name': self.name,
            'favorite_city': self.favorite_city,
            })
