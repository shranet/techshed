from django.urls import path
from .views import cart_change, cart_list, cart_checkout
from .views import OrderListView, order_pay


app_name = 'cart'
urlpatterns = [
    path('change/<str:action>-<int:pid>/', cart_change, name="change"),
    path('products/', cart_list, name="products"),
    path('checkout/', cart_checkout, name="checkout"),
    path('orders/', OrderListView.as_view(), name="orders"),
    path('pay/<int:oid>/', order_pay, name="pay")
]

