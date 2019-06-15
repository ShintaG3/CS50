from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm, RegisterForm, GuestForm
from django.utils.http import is_safe_url
from .models import GuestEmail

def guest_register_view(request):
    form_class = GuestForm(request.POST or None)
    context = {
         "form": form_class
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form_class.is_valid():
        email    = form_class.cleaned_data.get("email")
        print(email)
        print(form_class.cleaned_data['email'])
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register/")
    return redirect("/register/")

def login_page(request):
    form_class = LoginForm(request.POST or None)
    context = {
         "form": form_class
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form_class.is_valid():
        username = form_class.cleaned_data["username"]
        password = form_class.cleaned_data["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            # return an 'invalid login' error message.
            context['form_class'] = LoginForm()
    return render(request, "accounts/login.html", context)

User = get_user_model()
def register_page(request):
    form_class = RegisterForm(request.POST or None)
    context = {
        "form": form_class
    }
    if form_class.is_valid():
        print(form_class.cleaned_data)
        username = form_class.cleaned_data["username"]
        email = form_class.cleaned_data["email"]
        password = form_class.cleaned_data["password"]
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "accounts/register.html", context )
