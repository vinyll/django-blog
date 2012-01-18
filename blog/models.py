from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class ArticleManager(models.Manager):
    use_for_related_fields = True
    
    def published(self):
        return self.get_query_set().filter(is_published=True)

class Article(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(null=True)
    body = models.TextField()
    slug = models.SlugField()
    author = models.ForeignKey(User)
    is_published = models.BooleanField(default=False)
    publication_date = models.DateField(null=True)
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    
    objects = ArticleManager()
    
    def __unicode__(self):
        return unicode(self.title)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title
        self.slug = slugify(self.slug)
        super(Article, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('publication_date', 'creation_date')


class Comment(models.Model):
    body = models.TextField()
    author = models.CharField(max_length=20)
    author_email = models.EmailField()
    article = models.ForeignKey(Article)
    is_published = models.BooleanField(default=True)