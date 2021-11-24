import json
with open('/Users/hugo/Desktop/INFO_SITE/TDS/animal.json', "r") as f:
        animal = json.load(f)

with open('/Users/hugo/Desktop/INFO_SITE/TDS/équipement.json', "r") as f:
        equipement = json.load(f)

def lit_etat(animal_id):
    if animal_id in animal.keys():
        return animal[animal_id]['ETAT']
    else:
        print(f'Désolé, {animal_id} n\'est pas un animal connu')
        return None
def lit_lieu(animal_id):
    if animal_id in animal.keys():
        return animal[animal_id]['LIEU']
    else:
        print(f'Désolé, {animal_id} n\'est pas un animal connu')
        return None  

def verifie_disponibilite(equipement_id):
    if equipement_id in equipement.keys():
        return equipement[equipement_id]['DISPONIBILITÉ']
    else:
        print(f'Désolé, {equipement_id} n\'est pas un équipement connu')
        return None  

def cherche_occupant(lieu):
    liste = []
    if lieu in equipement.keys():
        for key in animal.keys():
            if animal[key]['LIEU'] == lieu:
                liste.append(key)
        return liste
    else:
        print(f'Désolé, {lieu} n\'est pas un lieu connu')
        return None

def change_etat(id_animal, etat):
    if etat in ['affamé', 'fatigué', 'repus', 'endormi']:
        if id_animal in animal.keys():
            animal[id_animal]['ETAT'] = etat
            with open('animal.json', "w") as g:
                json.dump(animal, g)
        else:
            print(f'Désolé, {id_animal} n\'est pas un animal connu')
            return None  
    else:
        print(f'Désolé, {etat} n\'est pas un état connu')
        return None

def change_lieu(id_animal, lieu):
    if (lieu in equipement.keys()) and (id_animal in animal.keys()):
        if equipement[lieu]['DISPONIBILITÉ'] == 'libre':
            ancien_lieu = animal[id_animal]['LIEU'] 
            equipement[ancien_lieu]['DISPONIBILITÉ'] = 'libre'
            animal[id_animal]['LIEU'] = lieu
            if lieu != 'litière':
                equipement[lieu]['DISPONIBILITÉ'] = 'occupé'
            with open('animal.json', "w") as g:
                json.dump(animal, g)  
            with open('equipement.json', "w") as g:
                json.dump(equipement, g)  
        else:
            print(f'Désolé, le lieu {lieu} est dejà occupé)')
            return None
    else:
        print(f'Désolé, le {lieu} n\'est pas connu ou l\'animal {id_animal} n\'existe pas')
        return None