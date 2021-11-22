from django.contrib import admin
from .models import Category, TopCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(TopCategory)
class TopCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'status')

