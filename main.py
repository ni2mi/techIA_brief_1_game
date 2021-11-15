import random
degats = 8
my_hp = 50
round = 1
lvl = 1 
enemy_hp = 30
ennemy_degats = 5
prenom = input("Quel est votre prenom ?")
choix_principal = input("Menu principal : \n Quel est votre choix ? \n 1 - start  \n 2 - score \n 3 - quitter ")
choix_combat = input (f"Que voulez_vous faire {prenom}") 
if round % 3 == 0 :
    lvl += 1 


def attaque(x) :                    # x =  Les points de vie ennemie ex : x = enemy["pv"]
    ''' Fonction pour l'attaque corp à corp   
    ---------------  
    Prend pour parametre x un int  '''
    return x - randint(5,10) 


def attaque_eclair(x):              # x =  Les points de vie ennemie 
    ''' Fonction pour l'attaque élcaire  
    ---------------  
    Prend pour parametre x un int  '''   
    return x - randint(9,12)

def attaque_groupee(x):             # x =  Les points de vie ennemie 
    ''' Fonction pour l'attaque groupé 
    ---------------  
    Prend pour parametre x un int  '''
    return x - randint(8,16)


# def attaque_ennemi(x):              # x =  Les points de vie de {prenom} 
#     '''  Fonction quand l'ennemie attaque 
#     ---------------  
#     Prend pour parametre x un int  '''
#     return x - randint(4,9)

 

def potion(x):                      # x =  Les points de vie de {prenom} 
    '''  Fonction pour ajouter 15 PV  
    ---------------  
    Prend pour parametre x un int  '''
    x+= 15  
    return x 
def maxipotion(x):                 # x =  Les points de vie de {prenom} 
    '''  Fonction pour ajouter 50 PV  
    ---------------  
    Prend pour parametre x un int  '''
    x += 50 
    return x 

def create_enemy(x): 
    x = {"enemy" : x , "PV" : 50}

    
def pop_enemy(x):                  # Fonction qui génère un nombre aléatoire entre 1 et 3 
    ''' Fonction qui génère aléatoirement entre 1 et 3 ennemi  
    ---------------  
    Prend pour parametre x un int  '''
    y = randint(1,3)
    
    return x * create_enemy(y)

 
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


