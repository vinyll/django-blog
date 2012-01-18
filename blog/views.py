from django.shortcuts import render
from django.shortcuts import get_object_or_404
from blog.models import Article

def index(request):
    articles = Article.objects.published()
    return render(request, 'blog/index.html', locals())

def show(request, slug):
    article = get_object_or_404(Article.objects.published(), slug=slug)
    return render(request, 'blog/show.html', locals())