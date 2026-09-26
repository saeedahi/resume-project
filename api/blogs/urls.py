from django.urls import path

from api.blogs.views import BlogListAPIView, BlogDetailAPIView

urlpatterns = [
    path('', BlogListAPIView.as_view(), name='blog-list-api'),
    path('<str:slug>/', BlogDetailAPIView.as_view(), name='blog-detail-api'),
]