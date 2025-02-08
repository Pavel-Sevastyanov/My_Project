from django.db import models


class Post(models.Model):
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Текстовые данные'

    def __str__(self):
        return self.text[:50]


class DatePost(models.Model):
    date = models.DateTimeField()

    def __str__(self):
        return self.date


class Book(models.Model):
    title = models.CharField(max_length=20, help_text='Enter name book')


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug  = models.SlugField(max_length=255, unique=True, verbose_name='URL имя')
    description = models.TextField(verbose_name='Описание')