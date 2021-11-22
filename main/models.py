from django.db import models
from django.utils.translation import get_language


class Category(models.Model):
    name_en = models.CharField(max_length=50)
    name_uz = models.CharField(max_length=50)

    @property
    def name(self):
        return getattr(self, f'name_{get_language()}')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class TopCategory(models.Model):
    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 0

    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    text_prefix = models.CharField(max_length=100)
    text = models.TextField()
    text_suffix = models.CharField(max_length=100)
    image = models.ImageField()
    status = models.SmallIntegerField(choices=(
        (STATUS_ACTIVE, "Active"),
        (STATUS_INACTIVE, "Inactive")
    ), default=STATUS_ACTIVE)

    class Meta:
        verbose_name = 'Top category'
        verbose_name_plural = 'Top categories'

