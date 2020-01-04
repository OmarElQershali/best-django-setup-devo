from django.conf import settings

from django.urls import path
from .views import base
urlpatterns = [
    path("", base, name="base")
]
