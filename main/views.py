from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AnimalForm, ContatoForm
from .models import Animal, Contato
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def home(request):
    animais_cadastrados =  [i for i in Animal.objects.all() if i.status == 1]
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


@login_required
def meus_animais(request):
    animals = [i for i in Animal.objects.all() if i.dono.email==request.user.email]
    contatos = []
    for a in animals:
        contatos.append(Contato.objects.filter(animal__id=a.id))
    context = {'animais': zip(animals, contatos) }
    return render(request, 'meus_animais.html', context)


@login_required
def animal_edit(request, id=None):
    animal = get_object_or_404(Animal, id=id)
    if request.method == 'POST':
        user_form = AnimalForm(request.POST, request.FILES, instance=animal)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('meus_animais'))
        else:
            return render(request, 'cadastrar_animal.html', {"form": user_form})
    else:
        user_form = AnimalForm(instance=animal)
        return render(request, 'cadastrar_animal.html', {"form": user_form})


@login_required
def animal_delete(request, id=None):
    animal = get_object_or_404(Animal, id=id)
    if request.method == 'POST':
        if animal.foto:
            animal.foto.delete()
        animal.delete()
        return HttpResponseRedirect(reverse('meus_animais'))
    else:
        context = {}
        context['user'] = animal
        return render(request, 'deletar_animal.html', context)

def animal_encontrado(request, id=None):
    context = {}
    animal = get_object_or_404(Animal, id=id)
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            animal.status = 2
            animal.save()
            instance.animal = animal
            instance.save()
            return redirect('home')
        else:
            context['form'] = form
    else:
        context['form'] = ContatoForm(request.POST)
    return render(request, 'animal_encontrado.html', context)
