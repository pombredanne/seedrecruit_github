from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^user/(?P<user>[a-zA-Z0-9]+)/$', 'seedrecruit.api.views.user', name='user'),
)
