"""
Definition of urls for Deal.
"""
from django.contrib import admin
from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url('admin/',admin.site.urls),
    url('',include('app1.urls')),
    # Examples:
    # url(r'^$', Deal.views.home, name='home'),
    # url(r'^Deal/', include('Deal.Deal.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
