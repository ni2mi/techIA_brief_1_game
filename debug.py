import fonction
import random


def pop_enemy():
    '''  This function create dictionnary of random enemy between 1 and 3 
    with prenamed random name 
    --------------
    This function doesn't need parameters '''
    c=0
    enemy_list = []
    name_list= ["Pythosore","Devosore","Simplosore","Tiranosor","Bigbob","Jevaismourir"]
    while c < random.randint(1,3):
        enemy_list.append({ "Name" : random.choice(name_list) , "PV" : random.randint(35,50)})
        c += 1 
    return enemy_list

enemy = pop_enemy()

cnt = 1 
for monstre in enemy:
    print(str(cnt) + " " + (monstre["Name"]))
    cnt += 1 


    
