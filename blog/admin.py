from django.contrib import admin
from django import forms
from blog.models import Article


class ArticleAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArticleAdminForm, self).__init__(*args, **kwargs)
        self.fields['slug'].required = False
        self.fields['summary'].required = False
        self.fields['publication_date'].required = False
    
    class Meta:
        model = Article

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm

admin.site.register(Article, ArticleAdmin)