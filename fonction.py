import random
def attack(x) :                    
    ''' Function to attack enemy by random between 5 and 10   
    ---------------  
    x should be an int  (Like x = enemy_HP) '''
    x -= random.randint(5,10) 
    return x 



def attack_lightning(x):              # x =  Les points de vie ennemie 
    ''' Function to attack enemy by random between 9 and 12
    ---------------  
    x should be an int  (Like x = enemy_HP)  '''   
    return x - random.randint(9,12)

def attack_group(x):             # x =  Les points de vie ennemie 
    ''' Function to attack group of enemy by random damages between 8 and 16
    ---------------  
    x should be an int  (Like x = enemy_HP)   '''
    return x - random.randint(8,16)


def enemy_attack(x):             
    ''' Function to attack playerHP 
    ---------------  
    x should be an int  (Like x = player_hp)  '''
    return x - random.randint(4,9)

 

def potion(x):                      # x =  Les points de vie de {prenom} 
    '''  This function add 15HP to HP_player 
    ---------------  
    x should be an int  (Like x = player_hp)  '''
    x+= 15  
    return x 
def max_potion(x):                 # x =  Les points de vie de {prenom} 
    '''  This function add 50HP to HP_player 
    ---------------  
    x should be an int  (Like x = player_hp)  '''
    x += 50 
    return x 
  
def pop_enemy():
    '''  This function create dictionnary of random enemy between 1 and 3 
    with prenamed random name 
    --------------
    This function doesn't need parameters '''
    c=0
    enemy_list = []
    name_list= ["Pythosore","Devosore","Simplosore","Tiranosor","Bigbob","Jevaismourir"]
    while c < random.randint(1,3):
        enemy_list.append({ "Name" : random.choice(name_list) , "HP" : random.randint(35,50)})
        c += 1 
    return enemy_list


 
 # Déclaration de nos variables 
degats = 8
my_hp = 50
round = 1
enemy_hp = 30
ennemy_degats = 5
# prenom = input("Quel est votre prenom ?")
# choix_principal = input("Menu principal : \n Quel est votre choix ? \n 1 - start  \n 2 - score \n 3 - quitter ")
# choix_combat = input (" Que voulez-vous faire ? \n option 1 : Attaque \n option 2 : Inventaire \n option 3 : fuir (Quitter la partie")
# choix_attaque = input (f"Que voulez_vous faire {prenom} ? \n option 1 : Attaque corp à corp \n option 2 : Attaque éclair \n option 3 : Attaque groupée ") 
# choix_inventaire = input ("Que voulez-vous faire ? \n option 1 : utiliser potion \n option 2 : Utiliser maxipotion")
# choix_enemy = input ("Qui voulez-vous attaquer : ")
