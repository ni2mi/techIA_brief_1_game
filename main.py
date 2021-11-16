# import 
import fonction 
import random 
import sys 

# commencement de la boucle : 
# leave = True 
enemies = fonction.pop_enemy()
leave = True 
while leave :

    prenom = input("Quel est votre prenom ?")
    print(f"Bonjour {prenom}")

    choix_principal = input("Menu principal : \n Quel est votre choix ? \n 1 - start  \n 2 - score \n 3 - quitter \n ")

    if choix_principal == '1' :
        print(f"le royaume se fait attaqué defendez le royaume de VS Code, tout les dev dependent de vous {prenom}")
        vague = 1 
        player = {"Name" : prenom , "potion" : 3, "potion_max" : 0, "HP" : 55}
        

        round = 0
        while player["HP"] >= 0 :
            print("Round :" , round)
            print(f"{prenom} : ", player["HP"] ," HP // Potion : ", player["potion" ] ," // Potion max : ", player["potion_max"])
            cnt = 1 
            print("Monstre(s) sur le terrain :")
            for monstre in enemies:
                print(monstre["Name"] , " " , monstre["HP"] , " HP")
            choix_combat = input (" Que voulez-vous faire ? \n option 1 : Attaque \n option 2 : Inventaire \n option 3 : fuir (Quitter la partie) \n ")
            # if choix_combat == "3" :
                # sys.exit("Vous avez quitter")
            combat = True 
            while combat :

                if choix_combat == "1" :

                    choix_attaque = input (f"Que voulez_vous faire {prenom} ? \n option 1 : Attaque corp à corp \n option 2 : Attaque éclair \n option 3 : Attaque groupée \n ") 
                    if choix_attaque == "1" :
                        cnt = 1 
                        for monstre in enemies:
                            print(str(cnt) + " " + monstre["Name"] + " " + str(monstre["HP"]))
                            cnt += 1 
                        choix_enemy = input("Qui voulez-vous attaquer : ")
                        enemies[int(choix_enemy) - 1]["HP"] = fonction.attack(enemies[int(choix_enemy) - 1]["HP"])
                        diff = player["HP"] 
                        player["HP"] = fonction.enemy_attack(player["HP"])
                        print(f"L'ennemi vous a attaqué \n{prenom} a perdu : ", diff - player["HP"], "HP" ,"\n") 
                        round += 1            
                        break

                    elif choix_attaque == "2" :
                        choix_enemy = input("Qui voulez-vous attaquer : ")
                        enemies[int(choix_enemy) - 1]["HP"] = fonction.attack_lightning(enemies[int(choix_enemy) - 1]["HP"])
                        diff = player["HP"] 
                        player["HP"] = fonction.enemy_attack(player["HP"])
                        print(f"L'ennemi vous a attaqué \n{prenom} a perdu : ", diff - player["HP"], "HP" ,"\n")   
                        round += 1          
                        break

                    elif choix_attaque == "3" :
                        for i in range(len(enemies)):
                            enemies[i]["HP"] = fonction.attack_group(enemies[i]["HP"])
                        diff = player["HP"] 
                        player["HP"] = fonction.enemy_attack(player["HP"])
                        print(f"L'ennemi vous a attaqué \n{prenom} a perdu : ", diff - player["HP"], "HP" ,"\n")     
                        round += 1        
                        break 
                    break

                    
                elif choix_combat == "2" :
                    print(f" Dans votre inventaire il y a " + str(player["potion"]) + " potion(s)")
                    choix_inventaire = input ("Que voulez-vous faire ? \n option 1 : utiliser potion \n option 2 : Utiliser maxipotion \n option 3 : Retour en arriere ")

                
                    if choix_inventaire == "1" : 
                        if player["potion"] > 0 : 
                            player["HP"] = fonction.potion(player["HP"])
                            player["potion"] -= 1
                            print ( " Vous avez : ", player["HP"] ," point de vie", "et " , player["potion"] , "potion(s)")
                            diff = player["HP"] 
                            player["HP"] = fonction.enemy_attack(player["HP"])
                            print(f"L'ennemi vous a attaqué \n{prenom} a perdu : ", diff - player["HP"], "HP" ,"\n")     
                            round += 1        
                            break
                        else: 
                            print("Vous n'avez plus de potion!")


                    elif choix_inventaire == "2" :
                        if player["potion_max"] > 0 :
                            player["HP"] = fonction.max_potion(player["HP"]) 
                            player["potion_max"] -= 1
                            print ( " Vous avez : ", player["HP"] ," point de vie", "et " , player["potion_max"] , "potion(s)") 
                            diff = player["HP"] 
                            player["HP"] = fonction.enemy_attack(player["HP"])
                            print(f"L'ennemi vous a attaqué \n{prenom} a perdu : ", diff - player["HP"], "HP" ,"\n")   
                            round += 1          
                            break 
                        else:
                            print("Mince! Vous n'avez plus de potion!")                       


                    elif choix_inventaire == "3" :
                        break 
                                                
                            

                    elif choix_combat == "3" : 
                        sys.exit("Vous avez quitter") 


    elif choix_principal == "3" : 
        sys.exit("Vous avez quitter")  

                


                    
                        
                                                    

                        










    elif choix_principal == 2:
        print("Score =")

    elif choix_principal == 3 :
        leave = False
        
        