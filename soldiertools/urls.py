
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'soldiertools.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	url(r'^admin/', include(admin.site.urls)),
	url(r'^salary/', include('salary.urls', namespace="salary")),
	url(r'^wages/', include('wages.urls', namespace="wages")),
)
