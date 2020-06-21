from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.Serializer):
    author_name=serializers.CharField(max_length=100)
    title=serializers.CharField(max_length=100)
    detail=serializers.CharField(max_length=500)
    created=serializers.DateTimeField(required=False)

    def create(self,validated_data):
        comment=Comment.objects.create(author_name=validated_data.get('author_name'),
                                title=validated_data.get('title'),
                                detail=validated_data.get('detail'),
                                created=validated_data.get('created'))
        return comment

    # def update(self, instance, validated_data):
    #     instance.author_name=validated_data.get('author_name',instance.author_name)