from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:post_new')


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    category = models.ManyToManyField(Category)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, default=True, null=True)
    post_time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, allow_unicode=True, default=None, null=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title, allow_unicode=True)
            default_len = len(slug)
            number = 1
            while True:
                try:
                    post = Post.objects.get(slug=slug)
                    if post == self:
                        self.slug = slug
                        break
                    else:
                        slug = slug[:default_len] + f'_{number}'
                        number += 1
                except:
                    self.slug = slug
                    break
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}--{self.post_time.strftime("%m/%d/%Y, %H:%M:%S")}'

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
