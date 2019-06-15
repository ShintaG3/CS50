from django.db import models
from django.db.models.signals import pre_save, post_save
import random
import os
from pizza2.utils import unique_slug_generator
from django.urls import reverse

# Create your models here.

def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(filename)
    return name, ext

def upload_image_path(instance, filename):
    # print(instance)
    # print(filename)
    new_filename = random.randint(1, 234324234)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )
class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self): # product.objects.featured()
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count()==1:
            return qs.first()
        return None

PRODUCT_CATEGORY = (
    ("regular-pizza","regular-pizza"),
    ("sicilian-pizza","sicilian-pizza"),
    ("subs","subs"),
    ("pasta","pasta"),
    ("salads","salads"),
    ("dinner","dinner"),
)

class Product(models.Model):
    #usually singular expression no Products
    #this class inherite models.Model
    category    = models.CharField(max_length=64, choices=PRODUCT_CATEGORY, default="regular-pizza")
    title       = models.CharField(max_length=64)
    topping_qty = models.PositiveIntegerField(default=0, null=True, blank=True)
    slug        = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=10, default=39.99)
    image       = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    objects     = ProductManager()
    featured    = models.BooleanField(default=False)
    active      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        # return "/product/{slug}/".format(slug=self.slug)
        return reverse("order:detail", kwargs={"slug": self.slug})


    def __str__(self):
        return f"{self.category} {self.title}"

    @property
    def name(self):
        return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)


class VariationManager(models.Manager):
    def all(self):
        return self.get_queryset().filter(active=True)

    def size(self):
        return self.all().filter(category='size')

    def topping(self):
        return self.all().filter(category='topping')

VAR_CATEGORY = (
    ('size', 'size'),
    ('topping', 'topping'),
    )

class Variation(models.Model):
    title       = models.CharField(max_length=64)
    products    = models.ManyToManyField(Product)
    category    = models.CharField(choices=VAR_CATEGORY, max_length=64, default='size')
    price       = models.DecimalField(max_digits=1000, decimal_places=2, null=True, blank=True)
    updated     = models.DateTimeField(auto_now_add=False, auto_now=True)
    active      = models.BooleanField(default=True)
    objects     = VariationManager()

    def __str__(self):
        return self.title
