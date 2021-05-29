from django.urls import path
from .views import field_view


urlpatterns = [
    path("", field_view.as_view(), name = "field_view")
]