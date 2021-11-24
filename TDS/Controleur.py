import Modele

def nourrir(animal_id):
    if Modele.verifie_disponibilite('mangeoire') == 'libre' and Modele.lit_etat(animal_id) == 'affamé':
            Modele.change_etat(animal_id,'repus')
            Modele.change_lieu(animal_id,'mangeoire')
            return f'Félicitations, {animal_id} a bien mange il est maintenant repus'
    else:
        if Modele.verifie_disponibilite('mangeoire') == 'occupé':
            liste = Modele.cherche_occupant('mangeoire')
            print(f'Impossible, le mangeoire est actuellement occupée par {liste[0]}')
            return f'Impossible, le mangeoire est actuellement occupée par {liste[0]}' 
        elif Modele.lit_etat(animal_id) != 'affamé':
            print(f'Désolé, {animal_id} n\'a pas faim!')
            return f'Désolé, {animal_id} n\'a pas faim!'
            
def divertir(animal_id):
    if Modele.verifie_disponibilite('roue') == 'libre' and Modele.lit_etat(animal_id) == 'repus':
            Modele.change_etat(animal_id,'fatigué')
            Modele.change_lieu(animal_id,'roue')
            return f'Félicitations, {animal_id} s\'est bien diverti il est maintenant fatigué'
    else:
        if Modele.verifie_disponibilite('roue') == 'occupé':
            liste = Modele.cherche_occupant('roue')
            print(f'Impossible, la roue est actuellement occupée par {liste[0]}')
            return f'Impossible, la roue est actuellement occupée par {liste[0]}' 
        elif Modele.lit_etat(animal_id) != 'repus':
            print(f'Désolé, {animal_id} n\'est pas en état de faire du sport!')
            return f'Désolé, {animal_id} n\'est pas en état de faire du sport!'

def coucher(animal_id):
    if Modele.verifie_disponibilite('nid') == 'libre' and Modele.lit_etat(animal_id) == 'fatigué':
            Modele.change_etat(animal_id,'endormi')
            Modele.change_lieu(animal_id,'nid')
            return f'Félicitations, {animal_id} s\'est couché il est maintenant endormi'
    else:
        if Modele.verifie_disponibilite('nid') == 'occupé':
            liste = Modele.cherche_occupant('nid')
            print(f'Impossible, le nid est actuellement occupée par {liste[0]}')
            return f'Impossible, le nid est actuellement occupée par {liste[0]}' 
        elif Modele.lit_etat(animal_id) != 'fatigué':
            print(f'Désolé, {animal_id} n\'est pas fatigué!')
            return f'Désolé, {animal_id} n\'est pas fatigué!'

def réveiller(animal_id):
    if Modele.lit_etat(animal_id) == 'endormi':
        Modele.change_lieu(animal_id,'litière')
        Modele.change_etat(animal_id,'affamé')  
        return f'Félicitations, {animal_id} s\'est bien réveillé il est desormais affamé' 
    else: 
        return f'Désolé, {animal_id} n\'est pas endormi'
    
