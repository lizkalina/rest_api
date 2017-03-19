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
        return json.loads(response.text)

    def create_person(self,info):
        person_details = json.loads(info)
        response = requests.post(_url('/people/'), json=person_details)
        return json.loads(response.text)

    def delete_person(self,pk):
        return requests.delete(_url('/people/{}/'.format(pk)))

    def update_person(self,pk,info):
        person_details = json.loads(info)
        response = requests.put(_url('/people/{}/'.format(pk)), json=person_details)
        return json.loads(response.text)
