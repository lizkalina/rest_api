from django.conf.urls import url, include
from .views import PersonDetail, PersonList

api_patterns = [
    url(r'people/(?P<pk>[0-9]+)\/?$', PersonDetail.as_view()),
    url(r'people/', PersonList.as_view()),
    ]
