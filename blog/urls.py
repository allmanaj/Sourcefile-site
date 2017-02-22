from django.conf.urls import url

from . import views

app_name='blog'
urlpatterns = [
    url(r'^$', views.feed, name='feed'),
    url(r'^new/$', views.new, name='new'),
    url(r'^new_post/$', views.new_post, name='new_post'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<post_id>[0-9]+)/post_comment/$', views.post_comment, name='post_comment'),
]
