from django.shortcuts import render,redirect
from .models import Etudiant
from .forms import AjoutForm

# Create your views here.
def index(request):
    etudiant=Etudiant.objects.all().order_by('create_at')
    return render(request, 'etudiant/index.html',{'etudiant':etudiant})

def blog(request):
    etudiant=Etudiant.objects.all().order_by('create_at')
    return render(request, 'etudiant/blog.html',{'etudiant':etudiant})

def ajout_etudiant(request):
    if request.method == "POST":
        form = AjoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Remplace par ta vue de redirection
    else:
        form = AjoutForm()

    return render(request, 'etudiant/ajout_etudiant.html', {'form': form})

def details(request,id):
    etudiant=Etudiant.objects.get(id=id)
    return render(request, 'etudiant/details.html',{'etudiant':etudiant})

def modifier_etudiant(request,id):
    etudiant=Etudiant.objects.get(id=id)
    if request.method == "POST":
        form = AjoutForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('index')  # Remplace par ta vue de redirection
    else:
        form = AjoutForm(instance=etudiant)

    return render(request, 'etudiant/modifier_etudiant.html', {'form': form})

def Supprimer_etudiant(request,id):
    liste= Etudiant.objects.get(id=id)
    liste.delete()
    return redirect('index')