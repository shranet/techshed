from django.urls import path
from .views import MainIndexView, MainAboutView, MainContactView, MainCategoryView, ProductView


app_name = 'main'

urlpatterns = [
    path('', MainIndexView.as_view(), name="index"),
    path('shop-all/', MainCategoryView.as_view(), name="shop-all"),
    path('sale/', MainCategoryView.as_view(discount=True), name="sale"),
    path('product-<int:pk>/', ProductView.as_view(), name="product"),
    path('category-<int:cat_id>/', MainCategoryView.as_view(), name="category"),
    path('about/', MainAboutView.as_view(), name="about"),
    path('contact/', MainContactView.as_view(), name="contact")
]
