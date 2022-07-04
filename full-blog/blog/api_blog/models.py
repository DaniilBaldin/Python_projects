from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True,
                               blank=True, default=None)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} -- {self.created_date.strftime("%d/%m/%Y, %H:%M")}'
