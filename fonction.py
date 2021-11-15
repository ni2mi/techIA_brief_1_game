import random
def attaque(x) :                    # x =  Les points de vie ennemie ex : x = enemy["pv"]
    ''' Fonction pour l'attaque corp à corp   
    ---------------  
    Prend pour parametre x un int  '''
    return x - random.randint(5,10) 


def attaque_eclair(x):              # x =  Les points de vie ennemie 
    ''' Fonction pour l'attaque élcaire  
    ---------------  
    Prend pour parametre x un int  '''   
    return x - random.randint(9,12)

def attaque_groupee(x):             # x =  Les points de vie ennemie 
    ''' Fonction pour l'attaque groupé 
    ---------------  
    Prend pour parametre x un int  '''
    return x - random.randint(8,16)


def attaque_ennemi(x):              # x =  Les points de vie de {prenom} 
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
def maxipotion(x):                 # x =  Les points de vie de {prenom} 
    '''  Fonction pour ajouter 50 PV  
    ---------------  
    Prend pour parametre x un int  '''
    x += 50 
    return x 

def create_enemy(): 
        '''  Fonction qui créer un monstre aléatoire entre 35-50 pv 
    ---------------  
    N'a pas besoin de parametre  '''
    liste = ["Pythosore","Devosore","Simplosore","Tiranosor","Bigbob","Jevaismourir"]
    x = { "Name" : random.choice(liste) , "PV" : random.randint(35,50)}
    return x 

    
def pop_enemy():                  # Fonction qui génère un nombre aléatoire entre 1 et 3 
    ''' Fonction qui génère aléatoirement entre 1 et 3 ennemi  
    ---------------  
    Prend pour parametre x un int  '''
    y = random.randint(1,3)
    x = y 
    return create_enemy()

 
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