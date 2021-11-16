import os
import sys
import inspect
import _ssl

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import main 

def test_potion(x):
    assert x == int 
    assert x > 0 

def test_maxipotion(x):
    assert type(x) == int 
    assert x > 0 

def test_attaque(x) :
    assert type(x) == int 
    assert x > 0 

def test_attaque_eclair(x):
    assert type(x) == int 
    assert x > 0 

def test_attaque_groupee(x):
    assert type(x) == int 
    assert x > 0 

def test_attaque_ennemi(x):
    assert type(x) == int 
    assert x > 0 

def test_pop_enemy(x):
    assert type(x) == int 
    assert x > 0 



def test_main_menu(x):
    assert input == True # ? 

# def lvlup(x):

