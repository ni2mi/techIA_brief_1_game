import os
import sys
import inspect
import _ssl

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 


import fonction 

def test_potion():
    assert fonction.potion(15) == 15 + 15

def test_maxi_potion():
    pv = 15 
    assert fonction.maxi_potion(pv) == 15 + 50

def test_attaque() :
    pv = 50 
    assert pv > fonction.attaque(pv)

def test_attaque_eclair():
    pv = 50 
    assert pv > fonction.attaque_eclair(pv)

def test_attaque_groupee():
    pv = 50 
    assert pv > fonction.attaque_groupee(pv)

def test_attaque_ennemi():
    pv = 50 
    assert pv > fonction.attaque_ennemi(pv)

def test_pop_enemy():
    assert type(fonction.pop_enemy()) == list 

def test_create_enemy(): 
    a = fonction.create_enemy()
    assert type(a) == dict 


