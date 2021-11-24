from django import forms

from .models import Animal,Equipement

class AnimalForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = ('race',)

class EquipementForm(forms.ModelForm):

    class Meta:
        model = Equipement
        fields = ('photo',)
