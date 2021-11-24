from django.urls import path
from .views import cart_change, cart_list, cart_checkout


app_name = 'cart'
urlpatterns = [
    path('change/<str:action>-<int:pid>/', cart_change, name="change"),
    path('products/', cart_list, name="products"),
    path('checkout/', cart_checkout, name="checkout")
]

