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
    test_attaque(50)
    assert  45 >= test_attaque(50) 

def test_attaque_eclair():
    pv = 50 
    assert fonction.attaque_eclair(pv) <= 41  

def test_attaque_groupee():
    pv = 50 
    assert 34 <= fonction.attaque_groupee(pv) <= 42

def test_attaque_ennemi():
    pv = 50 
    assert fonction.attaque_ennemi(pv) <= 46 

def test_pop_enemy():
    assert type(fonction.pop_enemy()) == list
    assert 50 >= fonction.pop_enemy()[0]["PV"] >= 35 