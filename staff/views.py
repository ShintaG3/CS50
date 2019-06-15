from django.shortcuts import render, redirect
from carts.models import Cart, CartItem
from orders.models import Order, ORDER_STATUS_CHOICES
from django.contrib.admin.views.decorators import staff_member_required
import carts

@staff_member_required
def CustomerOrders(request):
    orders = Order.objects.all()
    context = {
    "orders":orders
    }
    return render(request, "customer-order.html", context)

@staff_member_required
def CustomerOrder(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    view_only = True
    status_list = []
    for status in ORDER_STATUS_CHOICES:
        status_list.append(status[0])
    context = {
        "cart":cart,
        "view_only":view_only,
        "status":status_list,
    }
    return render(request, "home.html", context)

@staff_member_required
def Update(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    order = cart.order_cart.first()
    status = request.POST.get("status")
    order.status = status
    order.save()
    return redirect("staff:customer_orders")
