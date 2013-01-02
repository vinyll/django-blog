from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog.feeds import RssFeed, TagRssFeed


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='homepage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rss/$', RssFeed(), name="feed_rss"),
    url(r'^tag/(?P<slug>[-\w]+)/$', 'blog.views.articles_tag', name='blog_tag'),
    url(r'^tag/(?P<slug>[-\w]+)/rss/$', TagRssFeed(), name='tag_rss'),
    url(r'^(?P<slug>[-\w]+)/$', 'blog.views.show', name='blog_article'),
)
