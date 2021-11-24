from django.contrib import admin
from .models import Category, TopCategory, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'parent', 'name')


@admin.action(description='Active')
def top_category_make_active(modeladmin, request, queryset):
    queryset.update(status=TopCategory.STATUS_ACTIVE)


@admin.action(description='Inactive')
def top_category_make_inactive(modeladmin, request, queryset):
    queryset.update(status=TopCategory.STATUS_INACTIVE)


@admin.register(TopCategory)
class TopCategoryAdmin(admin.ModelAdmin):
    actions = [top_category_make_active, top_category_make_inactive]
    list_display = ('id', 'text', 'status')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('sold', )
    list_display = ('id', 'category', 'name', 'price', 'available')