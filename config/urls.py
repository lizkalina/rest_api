from django.conf.urls import url, include
from django.contrib import admin

from api.people.urls import api_patterns
#from restapp.urls import app_patterns

from restapp import views


urlpatterns = [
    url(r'^api/', include(api_patterns)),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^people/(?P<pk>[0-9]+)\/?$', views.detail, name='person_detail'),
    url(r'^people/new/$', views.new, {}, 'person_new'),
    url(r'^people/create/$', views.create, {}, 'person_create'),
    url(r'^people/edit/(?P<pk>\d+)\/?$', views.edit, {}, 'person_edit'),
    url(r'^people/update/(?P<pk>\d+)\/?$', views.update, {}, 'person_update'),
    url(r'^people/delete/(?P<pk>\d+)\/?$', views.delete, {}, 'person_delete'),
]
