from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipement, Animal
from .forms import AnimalForm, EquipementForm

def animal_list(request):
    animaux = Animal.objects.all()
    equipements = Equipement.objects.all()
    return render(request, 'animalerie/animal_list.html', {'animaux':animaux,'equipements':equipements})

def equipement_detail(request, pk):
    equipement = get_object_or_404(Equipement, pk=pk)
    return render(request, 'animalerie/equipement_detail.html', {'equipement': equipement})

def animal_modif(request,pk):
    animal = get_object_or_404(Animal, pk=pk)
    equipements = Equipement.objects.all()
    equipement = get_object_or_404(Equipement, pk=animal.lieu.id_equip)
    if request.method == "POST":
        if animal.etat == 'affamé':
            animal.etat = 'repus'
            equipement.disponibilite = 'libre'
            animal.lieu = Equipement.objects.filter(id_equip ="mangeoire")[0]
            equipement.save()
            equipement = get_object_or_404(Equipement, pk=animal.lieu.id_equip)
            equipement.disponibilite = 'occupé'
            equipement.save()
            animal.save()
            return redirect('animal_modif', pk=animal.pk)

        elif animal.etat == 'repus':
            animal.etat = 'fatigué'
            equipement.disponibilite = 'libre'
            animal.lieu = Equipement.objects.filter(id_equip ="roue")[0]
            equipement.save()
            equipement = get_object_or_404(Equipement, pk=animal.lieu.id_equip)
            equipement.disponibilite = 'occupé'
            equipement.save()
            animal.save()
            return redirect('animal_modif', pk=animal.pk)

        elif animal.etat == 'fatigué':
            animal.etat = 'endormi'
            equipement.disponibilite = 'libre'
            animal.lieu = Equipement.objects.filter(id_equip ="nid")[0]
            equipement.save()
            equipement = get_object_or_404(Equipement, pk=animal.lieu.id_equip)
            equipement.disponibilite = 'occupé'
            equipement.save()
            animal.save()
            return redirect('animal_modif', pk=animal.pk)

        elif animal.etat == 'endormi':
            animal.etat = 'affamé'
            equipement.disponibilite = 'libre'
            animal.lieu = Equipement.objects.filter(id_equip ="litière")[0]
            equipement.save()
            animal.save()
            return redirect('animal_modif', pk=animal.pk)
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'animalerie/animal_modif.html', {'form': form,"animal":animal,'equipements':equipements})