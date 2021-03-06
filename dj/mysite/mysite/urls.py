from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/conjugate/'}),
    url(r'^conjugate/$', 'conj.views.index'),
    url(r'^exercise/$', 'conj.views.exercise'),
    url(r'^about/$', 'conj.views.about'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
