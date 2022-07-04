import datetime

from django.utils import timezone
from rest_framework.generics import  GenericAPIView
from rest_framework.response import Response

from blog.models import Post
from blog.serializers import PostSerializer


class MyCustomMixin:
    def get_all_data(self, request):
        five_day_before = timezone.now() - datetime.timedelta(days=5)
        queryset = self.get_queryset().filter(created_date__gt=five_day_before).order_by('-created_date')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


class GetAllDataApiView(MyCustomMixin,
                        GenericAPIView):
    def get(self, request):
        return self.get_all_data(request)


class PostView(GetAllDataApiView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

