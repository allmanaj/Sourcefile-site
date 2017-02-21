from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.feed, name='feed'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
]
