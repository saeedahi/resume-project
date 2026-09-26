from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.blogs.serializers import BlogSerializer
from home.models import Article


class BlogListAPIView(ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Article.objects.all()


class BlogDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Article.objects.all().select_related('category')