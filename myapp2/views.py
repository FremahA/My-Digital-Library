from django.shortcuts import render

# Create your views here.
from .models import Article


def article_by_id(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'article_details.html', {'article':article})