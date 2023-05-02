from django.db import models
from django.urls import reverse


class Animal(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание')
    wiki_link = models.TextField(verbose_name='Ссылка на википедию')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    is_published = models.BooleanField(default=False, verbose_name='Опубликован')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Зверь'
        verbose_name_plural = 'Звери'
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
