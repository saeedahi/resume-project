from rest_framework import serializers
from home.models import Projects, Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            'id',
            'name',
        ]


class ProjectsSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(read_only=True, many=True)
    class Meta:
        model = Projects
        fields = '__all__'