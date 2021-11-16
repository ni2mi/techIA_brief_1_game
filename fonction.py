import random
def attack(x) :                    # x =  Les points de vie ennemie ex : x = enemy["pv"]
    ''' Fonction pour l'attaque corp à corp   
    ---------------  
    Prend pour parametre x un int  '''
    return x - random.randint(5,10) 


def attack_lightning(x):              # x =  Les points de vie ennemie 
    ''' Fonction pour l'attaque élcaire  
    ---------------  
    Prend pour parametre x un int  '''   
    return x - random.randint(9,12)

def attack_group(x):             # x =  Les points de vie ennemie 
    ''' Fonction pour l'attaque groupé 
    ---------------  
    Prend pour parametre x un int  '''
    return x - random.randint(8,16)


def enemy_attack(x):              # x =  Les points de vie de {prenom} 
    '''  Fonction quand l'ennemie attaque 
    ---------------  
    Prend pour parametre x un int  '''
    return x - random.randint(4,9)

 

def potion(x):                      # x =  Les points de vie de {prenom} 
    '''  Fonction pour ajouter 15 PV  
    ---------------  
    Prend pour parametre x un int  '''
    x+= 15  
    return x 
def max_potion(x):                 # x =  Les points de vie de {prenom} 
    '''  Fonction pour ajouter 50 PV  
    ---------------  
    Prend pour parametre x un int  '''
    x += 50 
    return x 
  
def pop_enemy():
    '''  Fonction pour creer entre 1 et 3 ennemis de nom 
    aleatoire dans une liste prédefinie 
    --------------
    ne prend pas d'argument'''
    c=0
    enemy_list = []
    name_list= ["Pythosore","Devosore","Simplosore","Tiranosor","Bigbob","Jevaismourir"]
    while c < random.randint(1,3):
        enemy_list.append({ "Name"+str(c+1) : random.choice(name_list) , "PV" : random.randint(35,50)})
        c += 1 
    return enemy_list

 
#Fonction principal de choix : 
# def main_menu(x):
#     leave = True 
#     if input == 1 :
#         #boucle while leave == True : choix ... 
#     if input == 2 : 
        
 
# Fonction qui va etre appeler a chaque round += 1 
# def lvlup(x):
# 	if round + 1 :
#         my_hp + 9 