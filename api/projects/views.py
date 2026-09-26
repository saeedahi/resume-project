from rest_framework.generics import ListAPIView
from api.projects.serializers import ProjectsSerializer
from home.models import Projects
from drf_spectacular.utils import extend_schema


class ProjectsListAPIView(ListAPIView):
    # @extend_schema(
    #     request=ProjectsSerializer,
    #     responses={201: ProjectsSerializer},
    # )
    serializer_class = ProjectsSerializer
    queryset = Projects.objects.all()