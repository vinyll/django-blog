from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='homepage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tag/(?P<slug>[-\w]+)/$', 'blog.views.articles_tag', name='blog_tag'),
    url(r'^(?P<slug>[-\w]+)/$', 'blog.views.show', name='blog_article'),
)
