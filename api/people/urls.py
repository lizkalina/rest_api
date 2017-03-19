from django.conf.urls import url, include
from rest_framework import routers
from .views import PersonDetail, PersonList
#import api.people.views as people_views

api_patterns = [
    url(r'^people/(?P<pk>[0-9]+)$', PersonDetail.as_view(), name='person-details'),
    url(r'^people/', PersonList.as_view(), name='people-list'),
    ]
