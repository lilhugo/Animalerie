from appJar import gui
import Modele
import Controleur
import json

with open('/Users/hugo/Desktop/INFO_SITE/TDS/animal.json', "r") as f:
        animal = json.load(f)

liste_animaux = ['Tic', 'Tac', 'Totoro', 'Patrick', 'Pocahontas']
liste_actions = ['nourrir','divertir','coucher','réveiller']
colour = ['lavender','left']
i = 0

app = gui()

app.addLabel("en-tête", "Bienvenue à l'animalerie !",0,0,3)
app.setLabelBg("en-tête", "salmon")
app.setLabelFg("en-tête", "white")

app.addLabel("titre", "Tableau de bord :",1,0,3)
app.setLabelBg("titre", "gray")
app.setLabelFg("titre", "white")

k=0
for elt in liste_animaux:
    app.addLabel(elt, f"{elt} ({animal[elt]['RACE']}) : {Modele.lit_etat(elt)}, {Modele.lit_lieu(elt)}",2+k,0,3)
    k += 1
    if i == 0:
        app.setLabelBg(elt, "lavender")
        i = 1
    else: i = 0

app.addLabel("titre2", "Actions :",7,0,3)
app.setLabelBg("titre2", "gray")
app.setLabelFg("titre2", "white")

i=0
for elt in liste_animaux: 
    app.addRadioButton("id_animal", elt,8+i,0)
    i += 1

i=0
for elt in liste_actions:
    app.addRadioButton("action", elt,8+i,1)
    i+=1

def press(act):

    id_animal = app.getRadioButton("id_animal")
    action = app.getRadioButton("action")

    if action == 'nourrir':
        result = Controleur.nourrir(id_animal)
        if result == f'Félicitations, {id_animal} a bien mangé il est maintenant repus':
            app.infoBox("SUCCÈS",result)
        else:
            app.warningBox("ERREUR",result)

    elif action == 'divertir':
        result = Controleur.divertir(id_animal)
        if result == f'Félicitations, {id_animal} s\'est bien diverti il est maintenant fatigué':
            app.infoBox("SUCCÈS",result)
        else:
            app.warningBox("ERREUR",result)

    elif action == 'coucher':
        result = Controleur.coucher(id_animal)
        if result == f'Félicitations, {id_animal} s\'est couché il est maintenant endormi':
            app.infoBox("SUCCÈS",result)            
        else:
            app.warningBox("ERREUR",result)

    else:
        result = Controleur.réveiller(id_animal)
        if result == f'Félicitations, {id_animal} s\'est bien réveillé il est désormais affamé':
            app.infoBox("SUCCÈS",result)            
        else:
            app.warningBox("ERREUR",result)

    app.setLabel(id_animal,f"{id_animal} ({animal[id_animal]['RACE']}) : {Modele.lit_etat(id_animal)}, {Modele.lit_lieu(id_animal)}")

app.addButton("go",press,8,2,0,5)

app.go()