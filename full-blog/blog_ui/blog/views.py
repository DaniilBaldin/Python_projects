from django.shortcuts import render


def home(request):
    return render(request, 'blog/base.html')


def postdetail(request, pk):
    return render(request, 'blog/post_detail.html', {'pk': pk})


def categoryposts(request, pk):
    return render(request, 'blog/category_posts.html', {'pk': pk})


def authorposts(request, pk):
    return render(request, 'blog/author_posts.html', {'pk': pk})
