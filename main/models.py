from django.db import models
from django.utils.translation import get_language


class Category(models.Model):
    parent = models.ForeignKey('Category', on_delete=models.RESTRICT, blank=True, null=True, default=None)
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


class Product(models.Model):
    STATUS_NEW = 0
    STATUS_APPROVED = 1
    STATUS_REJECTED = 2

    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    has_discount = models.BooleanField(default=False)
    discount_price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to="products/")
    available = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    status = models.SmallIntegerField(choices=(
        (STATUS_NEW, "New"),
        (STATUS_APPROVED, "Approved"),
        (STATUS_REJECTED, "Rejected")
    ), default=STATUS_NEW)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = (
            models.Index(fields=('status', '-sold', )),
        )
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
