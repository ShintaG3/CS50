from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .forms import ContactForm
from django.contrib.auth.decorators import permission_required
# Create your views here.

def index (request):
    context = {
    "":""
    }
    if request.user.is_authenticated:
        context["premiumcontent"] = "Yeahhhh"
        return render(request, "index.html", context)

    return render (request, "index.html", context)

def contact (request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render (request, "contact.html", context)
