from django.urls import path

from api.projects.views import ProjectsListAPIView

urlpatterns = [
    path('', ProjectsListAPIView.as_view(), name='projects-list-api'),
]