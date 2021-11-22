from django.urls import path
from .views import MainIndexView, MainAboutView, MainContactView


app_name = 'main'

urlpatterns = [
    path('', MainIndexView.as_view(), name="index"),
    path('about/', MainAboutView.as_view(), name="about"),
    path('contact/', MainContactView.as_view(), name="contact")
]
