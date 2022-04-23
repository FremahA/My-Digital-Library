from django.urls import path

from . import views

urlpatterns = [
    path('article/<int:article_id>', views.article_by_id, name='article_by_id'),
    ]