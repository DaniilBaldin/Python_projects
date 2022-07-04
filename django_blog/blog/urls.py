from django.urls import path

from .views import AuthorListView, PostDetailView, PostCreateView, \
    CategoryListView, CategoryAddView, PostUpdateView, PostDeleteView

app_name = 'blog'


urlpatterns = [
    path(r'/?P<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_new'),
    path('category/<pk>/', CategoryListView.as_view(), name='category_list'),
    path('add_category/', CategoryAddView.as_view(), name='add_category'),
    path('author/<author_pk>/', AuthorListView.as_view(), name='author_list'),
    path('<slug>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<slug>/delete/', PostDeleteView.as_view(), name='post_delete')
]
