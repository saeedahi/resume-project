from django.shortcuts import render
from django.views.generic import DetailView
from home.models import Article


# Create your views here.


class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    model = Article
    context_object_name = 'article'