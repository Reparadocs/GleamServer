from django.conf.urls import include, url
from rest_framework.authtoken import views as authviews
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^creative/info/', views.CreativeInfo.as_view(), name='creative_info'),
    url(r'^organization/info', views.OrganizationInfo.as_view(), name='organization_info'),
    url(r'^creative/search/', views.CreativeSearch.as_view(), name='creative_search'),
    url(r'^organization/search/', views.OrganizationSearch.as_view(), name='organization_search'),
    url(r'^creative/messages/(?P<pk>[0-9]+)$', views.CreativeMessages.as_view(), name='creative_messages'),
    url(r'^creative/get/(?P<pk>[0-9]+)$', views.CreativeGet.as_view(), name='creative_get'),
    url(r'^organization/get/(?P<pk>[0-9]+)$', views.OrganizationGet.as_view(), name='organization_get'),
    url(r'^creative/skills/(?P<pk>[0-9]+)$', views.CreativeSkills.as_view(), name='creative_messages'),
    url(r'^creative/types/(?P<pk>[0-9]+)$', views.CreativeTypes.as_view(), name='creative_messages'),
    url(r'^organization/skills/(?P<pk>[0-9]+)$', views.OrganizationSkills.as_view(), name='creative_messages'),
    url(r'^organization/messages/(?P<pk>[0-9]+)$', views.OrganizationMessages.as_view(), name='organization_messages')
]

urlpatterns = format_suffix_patterns(urlpatterns)