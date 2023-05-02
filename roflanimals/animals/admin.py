from django.contrib import admin
from .models import *


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'category', 'slug', 'is_published')
    list_display_links = ('id', 'name')
    list_editable = ('is_published',)
    search_fields = ('name', 'content')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Animal, AnimalAdmin)
admin.site.register(Category, CategoryAdmin)
