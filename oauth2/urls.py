from django.conf.urls import patterns, include, url
from rest_framework import routers
from apps.users import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
                       url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^', include(router.urls)),
                       # Examples:
                       # url(r'^$', 'oauth2.views.home', name='home'),
                       # url(r'^oauth2/', include('oauth2.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       )
