from rest_framework import serializers
from home.models import Article, Skill



class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            'id',
            'name',
        ]


class BlogSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)

    class Meta:
        model=Article
        fields='__all__'