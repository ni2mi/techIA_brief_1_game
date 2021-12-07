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

def test_max_potion():
    pv = 15 
    assert fonction.max_potion(pv) == 15 + 50

def test_attack() :
    assert  45 >= fonction.attack(50) 

def test_attack_lightning():
    pv = 50 
    assert fonction.attack_lightning(pv) <= 41  

def test_attack_group():
    pv = 50 
    assert 34 <= fonction.attack_group(pv) <= 42

def test_enemy_attack():
    pv = 50 
    assert fonction.enemy_attack(pv) <= 46 

def test_pop_enemy():
    assert type(fonction.pop_enemy()) == list
    assert 50 >= fonction.pop_enemy()[0]["HP"] >= 35 