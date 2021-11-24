from django.db import models

"""
Création des classes
"""
class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    def __str__(self):
        return self.id_equip

    def verifie_disponibilite(self):
            return self.disponibilite

class Animal(models.Model):
    id_animal = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    race = models.CharField(max_length=30)
    photo = models.CharField(max_length=200)
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_animal

    def lit_lieu(self):
            return self.lieu 

    def lit_etat(self):
            return self.etat

    def change_etat(self, etat):
        if etat in ['affamé', 'fatigué', 'repus', 'endormi']:
                self.etat = etat
        else:
            print(f'Désolé, {etat} n\'est pas un état connu')
    
    def change_lieu(self, lieu):
        if lieu in ["nid","roue","litière","mangeoire"]:
            if lieu == 'libre':
                self.lieu.disponibilite = 'libre'
                self.lieu = lieu
                if lieu != 'litière':
                    self.lieu.disponibilite = 'occupé'
            else:
                print(f'Désolé, le lieu {lieu} est dejà occupé)')
                return None
        else:
            print(f'Désolé, le {lieu} n\'est pas connu')
            return None
            
    def nourrir(self):
        self.change_etat('repus')
        self.change_lieu('mangeoire')
        return f'Félicitations, {self.id_animal} a bien mangé il est maintenant repus'
                
    def divertir(self):
        self.change_etat('fatigué')
        self.change_lieu('roue')
        return f'Félicitations, {self.id_animal} s\'est bien diverti il est maintenant fatigué'

    def coucher(self):
        self.change_etat('endormi')
        self.change_lieu('nid')
        return f'Félicitations, {self.id_animal} s\'est couché il est maintenant endormi'

    def reveiller(self):
        self.change_lieu('litière')
        self.change_etat('affamé')  
        return f'Félicitations, {self.id_animal} s\'est bien réveillé il est desormais affamé' 
