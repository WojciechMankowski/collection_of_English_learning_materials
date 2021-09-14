from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("see_url", see_urls, name="see"),
    path("add_url", add_url, name="add")
]
