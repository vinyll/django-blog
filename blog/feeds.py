from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse

from models import Article

from datetime import datetime, time
from markdown import markdown


class RssFeed(Feed):
    title = "Vinyll's blog"
    link = "/"
    description = "Python, Javascript and other Web development related stuff."

    def items(self):
        return Article.objects.all()[:10]

    def item_link(self, item):
        return reverse('blog_article', args=[item.slug])

    def item_author_name(self, item):
        return "%s %s" % (item.author.first_name, item.author.last_name)

    def item_description(self, item):
        return markdown(item.body)

    def item_pubdate(self, item):
        return datetime.combine(item.publication_date, time())
