from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("", views.cart_home, name="home"),
    path("update/", views.cart_update, name="update"),
    path("remove/", views.remove_from_cart, name="remove"),
    path("checkout/", views.checkout_home, name="checkout"),
    path("checkout/success/", views.checkout_done_view, name="success")
    # url(r'^product/(?P<slug>[\w-]+)/$', views.ProductDetailSlugView.as_view(), name="detail"),
]
