from django.urls import path
from . import views

urlpatterns = [
    path("get_token", views.get_auth_token),
    path("make_payment", views.make_payment)
]