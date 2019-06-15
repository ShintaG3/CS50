from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from . models import *
from carts.models import Cart
from django.views.generic import ListView, DetailView
# Create your views here.

class ProductFeaturedListView(ListView):
    template_name = "product/list.html"

    def get_queryset(self,*args,**kwargs):
        request = self.request
        category = category
        return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "product/featured-detail.html"

class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "product/list.html"
    #self.object_list is an instance of ListView
    def get_queryset(self):
        self.category = self.kwargs['category']
        print(self.category)
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

# def product_list_view(request):
#     queryset = Product.objects.all()
#     context = {
#         "object_list":queryset
#     }
#     return render(request, "product/list.html", context)

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "product/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhhhmmmm")
        return instance

class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "product/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product does not exist.")
        return instance

# def product_detail_view(request, pk=None, *args, **kwargs):
#     instance = Product.objects.get_by_id(pk)
#     if instance is None:
#         raise Http404("Product does not exist.")
#     context = {
#         "object":instance
#     }
#
#     return render(request, "product/detail.html", context)
