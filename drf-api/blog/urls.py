from django.urls import path

from blog.views import PostView

app_name = 'api'

urlpatterns = [
    path('posts/', PostView.as_view()),
    ]
