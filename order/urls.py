from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    # path("<int:pizza_id>", views.pizza, name="pizza"),
    # path("<int:pizza_id>/add", views.add, name="add"),
    path("product/<category>/", views.ProductListView.as_view(), name="list"),
    # url(r'^product/(?P<pk>\d+)/$', views.ProductDetailView.as_view()),
    url(r'^product/detail/(?P<slug>[\w-]+)/$', views.ProductDetailSlugView.as_view(), name="detail"),
    # path("product-fbv", views.product_list_view, name="product-fbv"),
    # url(r'^product-fbv/(?P<pk>\d+)/$', views.product_detail_view),
    # path("featured", views.ProductFeaturedListView.as_view(), name="featured"),
    # url(r'^featured/(?P<pk>\d+)/$', views.ProductFeaturedDetailView.as_view())
]
