from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm
from .forms import AuthenticationForm
# Create your views here.

# Create your views here.
def register(response):

    if response.method == "POST":
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        form = RegistrationForm()

    return render(response, "register/register.html", {"registration_form":form})


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
