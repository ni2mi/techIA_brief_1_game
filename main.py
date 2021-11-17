# import 
import fonction 
import random 
import sys 

# Déclaration des variables : 
error = "Error: Please use a correct number "
enemies = fonction.pop_enemy()
leave = True 
dead = 0       

while leave :           
    my_name = input("What's your name soldier?")
    print(f"Hi {my_name} !! We need your help!")

    menu_choice = input(f"Main menu : \n Make your choice {my_name} (Use number 1 - 2 - 3) \n 1 - Start  \n 2 - Score \n 3 - Exit \n ")

    if menu_choice == '1' :
        print("-----------------------------------------------------------")
        print(f"the kingdom is under attack! Defend the kingdom of VS Code, all depends on you {my_name}")
        player = {"Name" : my_name , "potion" : 3, "potion_max" : 0, "HP" : 55}
   
        round = 1
        while player["HP"] >= 0 and len(enemies) != 0 :
            print("-----------------------------------------------------------")
            print("Round :" , round)
            print(f"{my_name} : ", player["HP"] ," HP // Potion : ", player["potion" ] ," // Potion max : ", player["potion_max"])
            cnt = 1
            print("Monster on game :")
            for monster in enemies:
                print(monster["Name"] , " " , monster["HP"] , " HP")
            battle_choice = input ("Make your choice  \n  1 : Attack \n  2 : Iventory space \n  3 : Leave the game \n ")
            combat = True 
            while combat :

                if battle_choice == "1" :

                    attack_choice = input (f"Make your choice {my_name} ? \n 1 : Big punch \n 2 : Attack lightning \n 3 : Fire ball \n ")  
                    if attack_choice == "1" :
                        cnt = 1 
                        for monster in enemies:
                            print("Please use key " + str(cnt) + " for => " + monster["Name"] + " " + str(monster["HP"]))
                            cnt += 1 
                        target_choice = input(f"{my_name} : Who do you want to shoot ?")         
                        if int(target_choice) < 1 or int(target_choice) > len(enemies):
                            print(error)
                            break                         
                        diff_enemy = enemies[int(target_choice) - 1]["HP"] 
                        enemies[int(target_choice) - 1]["HP"] = fonction.attack(enemies[int(target_choice) - 1]["HP"])
                        print("\n Good shot! Enemy loose : -", diff_enemy - enemies[int(target_choice) - 1]["HP"], " HP")
                        diff = player["HP"] 
                        player["HP"] = fonction.enemy_attack(player["HP"])
                        print(f"\n Oh, now you are under attack!! \n{my_name} : -", diff - player["HP"], "HP lost!" ,"\n") 
                        round += 1            
                        break

                    elif attack_choice == "2" :
                        cnt = 1 
                        for monster in enemies:
                            print("Please use key " + str(cnt) + " for => "+ monster["Name"] + " " + str(monster["HP"]))
                            cnt += 1 
                        target_choice = input("Who do you want to shoot : ")
                        diff_enemy = enemies[int(target_choice) - 1]["HP"] 
                        enemies[int(target_choice) - 1]["HP"] = fonction.attack_lightning(enemies[int(target_choice) - 1]["HP"])
                        print("\n Good shot! Enemy loose :", diff_enemy - enemies[int(target_choice) - 1]["HP"], " HP")
                        diff = player["HP"] 
                        player["HP"] = fonction.enemy_attack(player["HP"])
                        print(f"\n Oh, now you are under attack!! \n{my_name} : -", diff - player["HP"], "HP lost!" ,"\n")  
                        round += 1          
                        break

                    elif attack_choice == "3" :
                        for i in range(len(enemies)):
                            diff_enemy = enemies[i]["HP"]
                            enemies[i]["HP"] = fonction.attack_group(enemies[i]["HP"])
                            print("\n Good shot! Enemy loose :", diff_enemy - enemies[i]["HP"], " HP!!")
                        diff = player["HP"] 
                        
                        player["HP"] = fonction.enemy_attack(player["HP"])
                        print(f"\n You are under attack!! \n{my_name} : -", diff - player["HP"], "HP lost!" ,"\n")    
                        round += 1        
                        break 
                    else:   # Print une erreur si l'input des choix d'attaque retourne une mauvaise valeurs 
                        print(error)
                    break
                


                    
                elif battle_choice == "2" :
                    print(f" They are : " + str(player["potion"]) + " potion in your bag")
                    choix_inventaire = input ("Make your choice {my_name} \n  1 : Use potion (+15HP) \n  2 : Use maxipotion (+50HP) \n  3 : Back ")                
                    if choix_inventaire == "1" : 
                        if player["potion"] > 0 : 
                            player["HP"] = fonction.potion(player["HP"])
                            player["potion"] -= 1
                            print ( " You feel better.. Now you have : ", player["HP"] ," HP", " and you have :" , player["potion"] , "potion in your bag")
                            diff = player["HP"] 
                            player["HP"] = fonction.enemy_attack(player["HP"])
                            print(f"You are under attack!! \n{my_name} : -", diff - player["HP"], "HP lost!" ,"\n")      
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
                            print(f"You are under attack!! \n{my_name} : -", diff - player["HP"], "HP lost!" ,"\n")  
                            round += 1          
                            break 
                        else:
                            print("You didn't have potion_max! !")    



                    elif choix_inventaire == "3" :
                        break
                    else:
                        print(error)
                        break 

                    
                        
                                                
                        
                elif battle_choice == "3" : 
                    sys.exit("You leave the game") 
                        
                else:
                    print(error)
                    break 
            dead = 0 
            for j in enemies :
                if j["HP"] <= 0 :
                    j["HP"] = 0
                    print(j["Name"] , "just died!")
                    dead +=1 
            if dead == len(enemies) :
                print ("You won!!")
                break
            if player["HP"] <= 0 :
                print ("Game Over!")
                break


    elif menu_choice == "3" : 
        leave = False 
        break
        
    else:
        print(error)
        continue
    




                
