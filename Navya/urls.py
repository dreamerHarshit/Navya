from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from Task import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'Navya.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^task/', include('Task.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
