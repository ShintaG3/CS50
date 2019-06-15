from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed
from django.conf import settings
from order.models import Product, Variation
from decimal import *

User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        print(user)
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)

class CartItem(models.Model):
    products    = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price  = models.DecimalField(max_digits=1000, decimal_places=2, default=10.99)
    variations  = models.ManyToManyField(Variation)
    cart        = models.ForeignKey('Cart', null=True, blank=True, on_delete=models.CASCADE) # read Cart laater
    quantity    = models.PositiveIntegerField(default=1)
    line_total  = models.DecimalField(default=10.99, decimal_places=2, max_digits=1000)
    timestamp   = models.DateTimeField(auto_now_add=True)
    # variations  = models.TextField(null=True, blank=True)

    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return self.products.title

class Cart(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    subtotal    = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    total       = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects     = CartManager()

    def __str__(self):
        return str(self.id)



def m2m_change_cartitem_receiver(sender, action, instance, *args, **kwargs):
    if action == 'pre_add' or 'pre_remove':
        if instance.variations:
            unit_price = 0
            for var in instance.variations.all():
                if not var.price is None:
                    unit_price += float(var.price)
                else:
                    pass
            if unit_price > 0:
                unit_price = unit_price
            else:
                unit_price = instance.products.price
        else:
            unit_price = instance.products.price
        instance.unit_price = unit_price
m2m_changed.connect(m2m_change_cartitem_receiver, sender=CartItem.variations.through)

def pre_save_cartitem_receiver(sender, instance, *args, **kwargs):
    instance.line_total = float(instance.unit_price) * float(instance.quantity)
pre_save.connect(pre_save_cartitem_receiver, sender=CartItem)

def post_save_cartitem_receiver(sender, instance, *args, **kwargs):
    try:
        cart = instance.cart
        items = cart.cartitem_set.all()
        total = 0
        for x in items:
            total += x.line_total
        if cart.subtotal != total:
            cart.subtotal = total
            cart.save()
    except:
        pass
post_save.connect(post_save_cartitem_receiver, sender=CartItem)


def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = float(instance.subtotal) * float(1.08)
    else:
        instance.total = 0.00

pre_save.connect(pre_save_cart_receiver, sender=Cart)
