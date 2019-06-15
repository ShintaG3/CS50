from django.shortcuts import render, redirect
from .models import Cart, CartItem
from order.models import Product, Variation
from orders.models import Order
from accounts.forms import LoginForm, GuestForm
from billing.models import BillingProfile
from accounts.models import GuestEmail
from addresses.forms import AddressForm
from addresses.models import Address

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "home.html", {"cart":cart_obj})

def remove_from_cart(request):
    if request.method == "POST":
        try:
            cart_id = request.session.get("cart_id", None)
            cart_obj = Cart.objects.get(id=cart_id)
        except:
            return redirect("cart:home")
        cart_item_id = request.POST.get("cart_item_id")
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.cart = None
        cart_item.save()

        request.session['cart_items'] = cart_obj.cartitem_set.count()
        return redirect("cart:home")

def cart_update(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        if product_id is not None:
            try:
                product_obj = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                print("Show message to use , product is gone?")
                return redirect("cart:home")

            qty = request.POST.get('product_quantity')
            if int(qty) > 0:

                product_variations = []
                try:
                    size = request.POST['size']
                    product_variations.append(size)
                except:
                    pass

                try:
                    toppings = request.POST.getlist('topping')
                    for topping in toppings:
                        product_variations.append(topping)
                except:
                    pass

                cart_obj, new_obj = Cart.objects.new_or_get(request)

                cart_item = CartItem.objects.create(cart=cart_obj, products=product_obj)

                if len(product_variations) > 0:
                    for item in product_variations:
                        # variation_set = Variation.objects.filter()
                        variation = Variation.objects.get(title=item, products=product_obj)
                        cart_item.variations.add(variation)
                cart_item.quantity = qty
                cart_item.save()

                request.session['cart_items'] = cart_obj.cartitem_set.count()
            return redirect("cart:home")

    return redirect("cart:home")

def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.cartitem_set.count()==0:
        return redirect("cart:home")

    login_form          = LoginForm()
    guest_form          = GuestForm()
    address_form        = AddressForm()
    billing_address_id  = request.session.get("billing_address_id", None)
    shipping_address_id = request.session.get("shipping_address_id", None)

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    address_qs = None
    if billing_profile is not None:
        if request.user.is_authenticated:
            address_qs = Address.objects.filter(billing_profile=billing_profile)
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)

        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
            del request.session["shipping_address_id"]
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            del request.session["billing_address_id"]
        if billing_address_id or shipping_address_id:
            order_obj.save()

    if request.method =="POST":
        "Check that order is done"
        is_done = order_obj.check_done()
        if is_done:
            order_obj.mark_paind()
            request.session["cart_items"] = 0
            del request.session["cart_id"]
            return redirect("cart:success")

    context = {
        "object":order_obj,
        "billing_profile": billing_profile,
        "login_form": login_form,
        "guest_form": guest_form,
        "address_form": address_form,
        "address_qs": address_qs,

    }
    return render(request, "checkout.html", context)

def checkout_done_view(request):
    return render(request, "checkout-done.html", {})
