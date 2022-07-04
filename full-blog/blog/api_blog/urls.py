from django.urls import path

from .views import AllPostView, SinglePostView, CategoriesPostView, CreatePostView, AuthorsPostView


urlpatterns = [
    path('all_posts/', AllPostView.as_view(), name='all_posts'),
    path('category_posts/<int:pk>', CategoriesPostView.as_view(), name='category_posts'),
    path('author_posts/<int:pk>', AuthorsPostView.as_view(), name='author_posts'),
    path('post/<int:pk>', SinglePostView.as_view(), name='post_detail'),
    path('post/create', CreatePostView.as_view(), name='post_create')
]
