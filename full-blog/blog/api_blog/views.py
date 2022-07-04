import random

import faker as Faker
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from urllib3.connectionpool import xrange

from .models import Post, Category, Author
from .serializers import PostSerializer
from random_word import RandomWords
import names


class AllPostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response({'posts': serializer.data})


class CategoriesPostView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = Post.objects.filter(category=category)
        return queryset

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response({'category_posts': serializer.data})


class AuthorsPostView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        author = get_object_or_404(Author, pk=self.kwargs['pk'])
        queryset = Post.objects.filter(author=author)
        return queryset

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response({'author_posts': serializer.data})


class SinglePostView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'post': serializer.data})


class CreatePostView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        if self.request.method == 'POST':
            all_users = list(User.objects.all())
            all_categories = list(Category.objects.all())
            fake = Faker()

            if len(all_categories) == 0:
                new_categories = set()
                while len(new_categories) < 20:
                    new_categories.add(fake.text(max_nb_chars=20))
                for cat in new_categories:
                    new_category = Category(name=cat)
                    new_category.save()
                all_categories = list(Category.objects.all())

            if len(all_users) <= 1:
                new_usernames = set()
                while len(new_usernames) < 10:
                    new_usernames.add(fake.first_name())
                for username in new_usernames:
                    new_user = User(username=username)
                    new_user.save()
                all_users = list(User.objects.all())

            random_title = fake.text(max_nb_chars=20)
            random_author = random.choice(all_users)
            random_category = random.choice(all_categories)
            random_text = fake.text()
            serializer.save(title=random_title, category=random_category, author=random_author, text=random_text)
            return
