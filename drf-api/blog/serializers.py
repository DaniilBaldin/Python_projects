from django.contrib.auth.models import User
from rest_framework.relations import SlugRelatedField
from rest_framework import serializers

from blog.models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'author', 'category', 'created_date', 'changed_date')

