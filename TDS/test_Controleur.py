import Controleur 
import Modele

def test_nourrir():
    if Modele.verifie_disponibilite('mangeoire') == 'libre' and Modele.lit_etat('Tic') == 'affamé':
        Controleur.nourrir('Tic')
    assert Modele.verifie_disponibilite('mangeoire') == 'occupé'
    assert Modele.lit_etat('Tic') == 'repus'
    assert Modele.lit_lieu('Tic') == 'mangeoire'
    Controleur.nourrir('Tac')
    assert Modele.lit_etat('Tac') == 'affamé'
    assert Modele.lit_lieu('Tac') == 'litière'
    Controleur.nourrir('Pocahontas')
    assert Modele.lit_etat('Pocahontas') == 'endormi'
    assert Modele.lit_lieu('Pocahontas') == 'nid'
    Controleur.nourrir('Bob')
    assert Modele.lit_etat('Bob') == None
    assert Modele.lit_lieu('Bob') == None
    assert Modele.verifie_disponibilite('mangeoire') == 'occupé'

def test_divertir():
    if Modele.verifie_disponibilite('roue') == 'libre' and Modele.lit_etat('Tic') == 'repus':
        Controleur.divertir('Tic')
    assert Modele.verifie_disponibilite('roue') == 'occupé'
    assert Modele.lit_etat('Tic') == 'fatigue'
    assert Modele.lit_lieu('Tic') == 'roue'
    Controleur.divertir('Tac')
    assert Modele.lit_etat('Tac') == 'repus'
    assert Modele.lit_lieu('Tac') == 'litière'
    Controleur.nourrir('Pocahontas')
    assert Modele.lit_etat('Pocahontas') == 'endormi'
    assert Modele.lit_lieu('Pocahontas') == 'nid'
    Controleur.divertir('Bob')
    assert Modele.lit_etat('Bob') == None
    assert Modele.lit_lieu('Bob') == None
    assert Modele.verifie_disponibilite('mangeoire') == 'occupé'