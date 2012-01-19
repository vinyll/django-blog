from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from mptt.models import MPTTModel, TreeForeignKey


class ArticlePublishedManager(models.Manager):
    use_for_related_fields = True
    
    def get_query_set(self, *args, **kwargs):
        queryset = super(ArticlePublishedManager, self).get_query_set(*args, **kwargs)
        return queryset.filter(is_published=True)

class Article(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(null=True)
    body = models.TextField()
    slug = models.SlugField()
    author = models.ForeignKey(User)
    tags = models.ManyToManyField('Tag')
    is_published = models.BooleanField(default=False)
    publication_date = models.DateField(null=True)
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    
    published = ArticlePublishedManager()
    
    @property
    def all_tags(self):
        """Returns a list a Tag that are related to this article"""
        return self.tags.all()[0].get_related(True)
    
    def __unicode__(self):
        return unicode(self.title)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title
        self.slug = slugify(self.slug)
        super(Article, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('publication_date', 'creation_date')


class Tag(MPTTModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def get_related(self, include_self=False):
        return self.get_ancestors(True, include_self)

    def __unicode__(self):
        return unicode(self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.name
        self.slug = slugify(self.slug)
        return super(Tag, self).save(self, *args, **kwargs)


class Comment(models.Model):
    body = models.TextField()
    author = models.CharField(max_length=20)
    author_email = models.EmailField()
    article = models.ForeignKey(Article)
    is_published = models.BooleanField(default=True)