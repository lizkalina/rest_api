"""spot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from api.people.urls import apipatterns

from restapp import views

urlpatterns = [
    url(r'^api/', include(apipatterns)),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^people/(?P<pk>[0-9]+)$', views.detail, name='person_detail'),
    url(r'^people/new/$', views.new, {}, 'person_new'),
    url(r'^people/create/$', views.create, {}, 'person_create'),
    url(r'^people/edit/(?P<pk>\d+)\/?$', views.edit, {}, 'person_edit'),
    url(r'^people/update/(?P<pk>\d+)\/?$', views.edit, {}, 'person_update'),
    url(r'^people/delete/(?P<pk>\d+)\/?$', views.delete, {}, 'person_delete'),
]
