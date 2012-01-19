from django.shortcuts import render
from django.shortcuts import get_object_or_404
from blog.models import Article, Tag

def index(request):
    articles = Article.published.all()
    return render(request, 'blog/index.html', locals())

def show(request, slug):
    article = get_object_or_404(Article.published, slug=slug)
    return render(request, 'blog/show.html', locals())

def articles_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    tags = tag.get_ancestors(True, True)
    descendants = tag.get_descendants(True)
    articles = Article.published.filter(tags__in=descendants)
    return render(request, 'blog/articles_tag.html', locals())