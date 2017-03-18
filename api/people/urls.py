from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(r'^people/$', 'person_list', name='person_list'),
    url(r'^people/(?P<pk>[0-9]+)$', 'person_detail', name='person_detail'),
)
