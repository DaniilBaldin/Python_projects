from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from .forms import PostForm, CategoryForm


from blog.models import Post, Category
# Create your views here.


class HomeView(generic.ListView):
    template_name = 'blog/base.html'
    context_object_name = 'post_list'
    model = Post
    queryset = Post.objects.filter(
            post_time__lte=timezone.now()).order_by('post_time')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True


class CategoryListView(generic.ListView):
    template_name = 'blog/category_list.html'
    model = Category

    def get_queryset(self):
        return Category.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(
            category=self.kwargs['pk']).order_by('post_time')
        context['category_list'] = Category.objects.all()
        return context


class AuthorListView(generic.ListView):
    model = User
    template_name = 'blog/author_posts.html'

    def get_queryset(self):
        return Post.objects.filter(
            author=self.kwargs['author_pk']).order_by('post_time')


class CategoryAddView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      generic.CreateView):
    model = Category
    template_name = 'blog/add_category.html'
    form_class = CategoryForm
    permission_required = 'admin'


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,
                     generic.UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'blog/post_edit.html'


class PostDeleteView(LoginRequiredMixin,
                     generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
