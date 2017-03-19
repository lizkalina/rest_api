import requests
import json
from helpers import _url
import pdb

class PersonService:

    def get_people(self):
        response = requests.get(_url('/people/'))
        return json.loads(response.text)

    def get_person(self,pk):
        response = requests.get(_url('/people/{}/'.format(pk)))
        pdb.set_trace()
        return json.loads(response.text)

    def create_person(self,name,favorite_city):
        return requests.post(_url('/people/'), json={
            'name': name,
            'favorite_city': favorite_city,
            })

    def delete_person(self,pk):
        return requests.delete(_url('/people/{}/'.format(pk)))

    def update_person(self,pk,name,favorite_city):
        url = _url('/people/{}/'.format(self.pk))
        return requests.put(url, json={
            'name': self.name,
            'favorite_city': self.favorite_city,
            })
