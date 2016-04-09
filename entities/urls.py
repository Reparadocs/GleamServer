from django.conf.urls import include, url
from rest_framework.authtoken import views as authviews
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^creative/info/', views.CreativeInfo.as_view(), name='creative_info'),
    url(r'^organization/info', views.OrganizationInfo.as_view(), name='organization_info'),
    url(r'^project/list/', views.ProjectInfo.as_view(), name='project_info'),
    url(r'^project/create/(?P<pk>[0-9]+)$', views.CreateProject.as_view(), name='create_project'),
    url(r'^creative/search/', views.CreativeSearch.as_view(), name='creative_search'),
    url(r'^organization/search/', views.OrganizationSearch.as_view(), name='organization_search'),
    url(r'^project/search/', views.ProjectSearch.as_view(), name='project_search'),
    url(r'^creative/messages/(?P<pk>[0-9]+)$', views.CreativeMessages.as_view(), name='creative_messages'),
    url(r'^creative/skills/(?P<pk>[0-9]+)$', views.CreativeSkills.as_view(), name='creative_messages'),
    url(r'^creative/types/(?P<pk>[0-9]+)$', views.CreativeTypes.as_view(), name='creative_messages'),
    url(r'^projects/skills/(?P<pk>[0-9]+)$', views.ProjectSkills.as_view(), name='creative_messages'),
    url(r'^organization/messages/(?P<pk>[0-9]+)$', views.OrganizationMessages.as_view(), name='organization_messages')
]

urlpatterns = format_suffix_patterns(urlpatterns)