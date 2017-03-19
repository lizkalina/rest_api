from django.conf.urls import url, include
from django.contrib import admin

from api.people.urls import api_patterns
from restapp.urls import app_patterns

urlpatterns = [
    url(r'^api/', include(api_patterns)),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(app_patterns)),
]
