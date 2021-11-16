# import 
import fonction 
import random 
import sys 

# Déclaration des variables : 
error = "Error: Please use number tuch"
enemies = fonction.pop_enemy()
leave = True 
                                                                                               
while leave :           
    prenom = input("What's your name soldier?")
    print(f"Hi {prenom} !! We need your help!")

    choix_principal = input(f"Main menu : \n Make your choice {prenom} (Use tuch 1 - 2 - 3) \n 1 - Start  \n 2 - Score \n 3 - Exit \n ")

    if choix_principal == '1' :
        print("-----------------------------------------------------------")
        print(f"the kingdom is under attack! Defend the kingdom of VS Code, all depends on you {prenom}")
        vague = 1 
        player = {"Name" : prenom , "potion" : 3, "potion_max" : 0, "HP" : 55}
        
        
        round = 0
        while player["HP"] >= 0 :
            print("-----------------------------------------------------------")
            print("Round :" , round)
            print(f"{prenom} : ", player["HP"] ," HP // Potion : ", player["potion" ] ," // Potion max : ", player["potion_max"])
            cnt = 1 
            print("Monster on game :")
            for monstre in enemies:
                print(monstre["Name"] , " " , monstre["HP"] , " HP")
            choix_combat = input ("Make your choice  \n  1 : Attack \n  2 : Iventory space \n  3 : Leave the game \n ")
            combat = True 
            while combat :

                if choix_combat == "1" :

                    choix_attaque = input (f"Make your choice {prenom} ? \n 1 : Big punch \n 2 : Attack lightning \n 3 : Fire ball \n ")  
                    if choix_attaque == "1" :
                        cnt = 1 
                        for monstre in enemies:
                            print("Tuch " + str(cnt) + " for => " + monstre["Name"] + " " + str(monstre["HP"]))
                            cnt += 1 
                        choix_enemy = input(f"{prenom} : Who do you want to shoot ?")
                        if choix_enemy != str(int) :
                            print(error)
                            break
                        diff_enemy = enemies[int(choix_enemy) - 1]["HP"] 
                        enemies[int(choix_enemy) - 1]["HP"] = fonction.attack(enemies[int(choix_enemy) - 1]["HP"])
                        print("\n Good shot! Enemy loose :", diff_enemy - enemies[int(choix_enemy) - 1]["HP"], " HP")
                        diff = player["HP"] 
                        player["HP"] = fonction.enemy_attack(player["HP"])
                        print(f"\n Oh, now you are under attack!! \n{prenom} : -", diff - player["HP"], "HP lost!" ,"\n") 
                        round += 1            
                        break

                    elif choix_attaque == "2" :
                        cnt = 1 
                        for monstre in enemies:
                            print("Tuch " + str(cnt) + " for => "+ monstre["Name"] + " " + str(monstre["HP"]))
                            cnt += 1 
                        choix_enemy = input("Who do you want to shoot : ")
                        diff_enemy = enemies[int(choix_enemy) - 1]["HP"] 
                        enemies[int(choix_enemy) - 1]["HP"] = fonction.attack_lightning(enemies[int(choix_enemy) - 1]["HP"])
                        print("\n Good shot! Enemy loose :", diff_enemy - enemies[int(choix_enemy) - 1]["HP"], " HP")
                        diff = player["HP"] 
                        player["HP"] = fonction.enemy_attack(player["HP"])
                        print(f"\n Oh, now you are under attack!! \n{prenom} : -", diff - player["HP"], "HP lost!" ,"\n")  
                        round += 1          
                        break

                    elif choix_attaque == "3" :
                        for i in range(len(enemies)):
                            diff_enemy = enemies[i]["HP"]
                            enemies[i]["HP"] = fonction.attack_group(enemies[i]["HP"])
                            print("\n Good shot! Enemy loose :", diff_enemy - enemies[i]["HP"], " HP!!")
                        diff = player["HP"] 
                        player["HP"] = fonction.enemy_attack(player["HP"])
                        print(f"\n You are under attack!! \n{prenom} : -", diff - player["HP"], "HP lost!" ,"\n")    
                        round += 1        
                        break 
                    else:   # Print une erreur si l'input des choix d'attaque retourne une mauvaise valeurs 
                        print(error)
                    break
                


                    
                elif choix_combat == "2" :
                    print(f" They are : " + str(player["potion"]) + " potion in your bag")
                    choix_inventaire = input ("Make your choice {prenom} \n  1 : Use potion (+15HP) \n  2 : Use maxipotion (+50HP) \n  3 : Back ")                
                    if choix_inventaire == "1" : 
                        if player["potion"] > 0 : 
                            player["HP"] = fonction.potion(player["HP"])
                            player["potion"] -= 1
                            print ( " You feel better.. Now you have : ", player["HP"] ," HP", " and you have :" , player["potion"] , "potion in your bag")
                            diff = player["HP"] 
                            player["HP"] = fonction.enemy_attack(player["HP"])
                            print(f"You are under attack!! \n{prenom} : -", diff - player["HP"], "HP lost!" ,"\n")      
                            round += 1        
                            break
                        else: 
                            print("You didn't have potion! ")


                    elif choix_inventaire == "2" :
                        if player["potion_max"] > 0 :
                            player["HP"] = fonction.max_potion(player["HP"]) 
                            player["potion_max"] -= 1
                            print ( " You feel better.. Now you have : ", player["HP"] ," HP", " and you have :" , player["potion"] , "potion in your bag")
                            diff = player["HP"] 
                            player["HP"] = fonction.enemy_attack(player["HP"])
                            print(f"You are under attack!! \n{prenom} : -", diff - player["HP"], "HP lost!" ,"\n")  
                            round += 1          
                            break 
                        else:
                            print("You didn't have potion_max! !")    



                    elif choix_inventaire == "3" :
                        break
                    else:
                        print(error)
                        break 

                    
                        
                                                
                        
                elif choix_combat == "3" : 
                    sys.exit("You leave the game") 
                        
                else:
                    print(error)
                    break 


    elif choix_principal == "3" : 
        continue
        
    else:
        leave = False 
        print(error)
        break
    break




                
