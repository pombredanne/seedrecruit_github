from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/', include('seedrecruit.api.urls', namespace='api')),
    # url(r'^$', 'seedrecruit.views.home', name='home'),
)
