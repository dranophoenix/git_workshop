from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'git_workshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^aaadminarairor/', include(admin.site.urls)),
)
