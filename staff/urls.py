from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path("", views.CustomerOrders, name="customer_orders"),
    path("customer_order/<cart_id>", views.CustomerOrder, name="customer_order"),
    path("update/<cart_id>", views.Update, name="update"),
]
