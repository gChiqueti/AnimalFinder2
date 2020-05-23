from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm
from .forms import AuthenticationForm
# Create your views here.

# Create your views here.
def register(response):
    context = {}
    if response.method == "POST":
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect("home")
        else:
            print(form.errors)
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(response, "register/register.html", context)


def user_login(request):
     context = {}
     user = request.user
     if user.is_authenticated:
        return redirect("home")

     if request.POST:
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            email    = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
     else:
        form = AuthenticationForm()

     context['login_form'] = form
     return render(request, 'login/login.html', context)

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('home'))
