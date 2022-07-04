from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='all_post'),
    path('post/<int:pk>', views.postdetail, name='post_detail'),
    path('category_posts/<int:pk>', views.categoryposts, name='category_posts'),
    path('author_posts/<int:pk>', views.authorposts, name='author_posts')
]
