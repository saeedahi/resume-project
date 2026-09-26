from django.urls import path

from blog.views import BlogDetailView

urlpatterns = [
    path('<str:slug>/', BlogDetailView.as_view(), name='blog_detail'),
]