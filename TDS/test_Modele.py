import Modele 
 
def test_lit_etat():
    assert Modele.lit_etat('Tac') == 'affamé'
 
def test_lit_etat_nul():
    assert Modele.lit_etat('Bob') == None

def test_lit_lieu():
    assert Modele.lit_lieu('Tac') == 'litière'
 
def test_lit_lieu_nul():
    assert Modele.lit_lieu('Bob') == None

def test_verifie_disponibilite():
    assert Modele.verifie_disponibilite('litière') == 'libre'
    assert Modele.verifie_disponibilite('nid') == 'occupé'

def test_verifie_disponibilite_nul():
    assert Modele.verifie_disponibilite('nintendo') == None

def test_cherche_occupant():
    assert Modele.cherche_occupant('nid') == ['Pocahontas']
    assert 'Tac' in Modele.cherche_occupant('litière')
    assert 'Tac' not in Modele.cherche_occupant('mangeoire')

def test_cherche_occupant_nul():
    assert Modele.cherche_occupant('casino') == None

def test_change_etat():
    Modele.change_etat('Totoro', 'fatigué')
    assert Modele.lit_etat('Totoro') == 'fatigué'
    Modele.change_etat('Totoro', 'excite comme un pou')
    assert Modele.lit_etat('Totoro') == 'fatigué'
    Modele.change_etat('Bob', 'fatigué')
    assert Modele.lit_etat('Bob') == None

def test_change_lieu():
    Modele.change_lieu('Totoro', 'roue')
    assert Modele.lit_lieu('Totoro') == 'roue'
    assert Modele.verifie_disponibilite('mangeoire') == 'libre'    
    assert Modele.verifie_disponibilite('roue') == 'occupé'   

def test_change_lieu_occupé():
    Modele.change_lieu('Totoro', 'nid')
    assert Modele.lit_lieu('Totoro') == 'roue'

def test_change_lieu_nul_1():
    Modele.change_lieu('Totoro', 'casino')
    assert Modele.lit_lieu('Totoro') == 'roue'

def test_change_lieu_nul_2():
    Modele.change_lieu('Bob', 'litière')
    assert Modele.lit_lieu('Bob') == None
