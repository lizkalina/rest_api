from django.conf.urls import url, include

from restapp import views

app_patterns = [
    url(r'^$', views.index, name='index'),
    url(r'people\/?$', views.index, name='index'),
    url(r'^people/(?P<pk>[0-9]+)\/?$', views.detail, name='person_detail'),
    url(r'^people/new/$', views.new, {}, 'person_new'),
    url(r'^people/create/$', views.create, {}, 'person_create'),
    url(r'^people/edit/(?P<pk>\d+)\/?$', views.edit, {}, 'person_edit'),
    url(r'^people/update/(?P<pk>\d+)\/?$', views.update, {}, 'person_update'),
    url(r'^people/delete/(?P<pk>\d+)\/?$', views.delete, {}, 'person_delete'),
]
