from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AnimalForm
from .models import Animal
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def home(request):
    animais_cadastrados = Animal.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(animais_cadastrados, 5)
    try:
        animais_cadastrados = paginator.page(page)
    except PageNotAnInteger:
        animais_cadastrados = paginator.page(1)
    except EmptyPage:
        animais_cadastrados = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'animais_cadastrados': animais_cadastrados})


@login_required
def cadastrar_animal(request):
    form = AnimalForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.dono = request.user
        instance.save()

        return redirect('home')
    return render(request, 'cadastrar_animal.html', {'form': form})
