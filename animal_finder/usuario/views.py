from django.shortcuts import render, redirect, reverse
from .forms import RegistrationForm
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
