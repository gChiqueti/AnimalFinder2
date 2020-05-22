from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AnimalForm

# Create your views here.

def home(response):
    return render(response, "home.html")


@login_required
def cadastrar_animal(request):
    form = AnimalForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.dono = request.user
        print(instance.foto)
        instance.save()

        return redirect('home')
    return render(request, 'cadastrar_animal.html', {'form': form})
