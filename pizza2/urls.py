from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from accounts.views import login_page, register_page, guest_register_view
from addresses.views import checkout_address_create_view, checkout_address_reuse_view

urlpatterns = [

    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("login/", login_page, name="login_page"),
    path("register/guest", guest_register_view, name="guest_register"),
    path("logout/", LogoutView.as_view(), name="logout_page"),
    path("checkout/address/create/", checkout_address_create_view, name="checkout_address_create"),
    path("checkout/address/reuse/", checkout_address_reuse_view, name="checkout_address_reuse"),
    path("register", register_page, name="register_page"),
    path('', include(('order.urls', 'order'), namespace='order')),
    path('cart/', include(('carts.urls', 'carts'), namespace='cart')),
    path('admin/', admin.site.urls),
    path('bootstrap', TemplateView.as_view(template_name='bootstrap/example.html') ),
    path('staff/', include(('staff.urls', 'staff'), namespace='staff'))

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
