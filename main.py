import fonction 
import random 
import sys 
import csv
import os.path

# Déclaration des variables : 
error = "Error: Please use a correct number "
enemies = fonction.pop_enemy()
leave = True 
dead = 0       

while leave : # program starting loop
    my_name = input("What's your name soldier?") 
    print(f"Hi {my_name} !! We need your help!")

    menu_choice = input(f"Main menu : \n Make your choice {my_name} (Use number 1 - 2 - 3) \n 1 - Start  \n 2 - Score \n 3 - Exit \n ")

    if menu_choice == '1' : # we enter the game when we select start
        print("-----------------------------------------------------------")
        print(f"the kingdom is under attack! Defend the kingdom of VS Code, all depends on you {my_name}")
        player = {"Name" : my_name , "potion" : 3, "potion_max" : 0, "HP" : 55}
   
        round = 1
        while player["HP"] >= 0 and len(enemies) != 0 : #when we die or an enemy is defeated the game stops 
            print("-----------------------------------------------------------")
            print("Round :" , round)
            print(f"{my_name} : ", player["HP"] ," HP // Potion : ", player["potion" ] ," // Potion max : ", player["potion_max"])
    
            print("Monster on game :")
            for monster in enemies: # we show the remaining enemies 
                print(monster["Name"] , " " , monster["HP"] , " HP")
            battle_choice = input ("Make your choice  \n  1 : Attack \n  2 : Inventory space \n  3 : Leave the game \n ")

            combat = True 
            while combat : # we start the adventure

                if battle_choice == "1" : # we start the attack against enemies

                    attack_choice = input (f"Make your choice {my_name} ? \n 1 : Big punch \n 2 : Attack lightning \n 3 : Fire ball \n ")  
                    if attack_choice == "1" : # we send player attack Big punch

                        cnt = 1 
                        for monster in enemies: # we show how to target the ennemy
                            print("Please use key " + str(cnt) + " for => " + monster["Name"] + " " + str(monster["HP"]))
                            cnt += 1 
                        target_choice = input(f"{my_name} : Who do you want to shoot ?") # we ask the player to target the enemy he wants to attack

                        if int(target_choice) < 1 or int(target_choice) > len(enemies): # if the player inputs the wrong target we send him back an error
                            print(error)
                            break        

                        diff_enemy = enemies[int(target_choice) - 1]["HP"] 
                        enemies[int(target_choice) - 1]["HP"] = fonction.attack(enemies[int(target_choice) - 1]["HP"]) # we substract the hp from the enemy hp after we attacked him
                        print("\n Good shot! Enemy loose : -", diff_enemy - enemies[int(target_choice) - 1]["HP"], " HP")
                        diff = player["HP"] 
                        player["HP"] = fonction.enemy_attack(player["HP"]) # we sustract the hp from the player hp after he got attacked
                        print(f"\n Oh, now you are under attack!! \n{my_name} : -", diff - player["HP"], "HP lost!" ,"\n") 
                        round += 1            
                        break

                    elif attack_choice == "2" : # we send player attack named attack lightning

                        cnt = 1 
                        for monster in enemies: # we show how to target the ennemy
                            print("Please use key " + str(cnt) + " for => "+ monster["Name"] + " " + str(monster["HP"]))
                            cnt += 1 
                        target_choice = input("Who do you want to shoot : ") # we ask the player to target the enemy he wants to attack
                        diff_enemy = enemies[int(target_choice) - 1]["HP"] 
                        enemies[int(target_choice) - 1]["HP"] = fonction.attack_lightning(enemies[int(target_choice) - 1]["HP"]) # we substract the hp from the enemy hp after we attacked him
                        print("\n Good shot! Enemy loose :", diff_enemy - enemies[int(target_choice) - 1]["HP"], " HP")
                        diff = player["HP"] 
                        player["HP"] = fonction.enemy_attack(player["HP"]) # we sustract the hp from the player hp after he got attacked
                        print(f"\n Oh, now you are under attack!! \n{my_name} : -", diff - player["HP"], "HP lost!" ,"\n")  
                        round += 1          
                        break

                    elif attack_choice == "3" : # we send player attack named fire ball

                        for i in range(len(enemies)): # we target all enemies with this attack
                            diff_enemy = enemies[i]["HP"] 
                            enemies[i]["HP"] = fonction.attack_group(enemies[i]["HP"]) # we substract the hp from the enemies hp after we attacked them
                            print("\n Good shot! Enemy loose :", diff_enemy - enemies[i]["HP"], " HP!!")
                        diff = player["HP"] 
                        
                        player["HP"] = fonction.enemy_attack(player["HP"]) # we sustract the hp from the player hp after he got attacked
                        print(f"\n You are under attack!! \n{my_name} : -", diff - player["HP"], "HP lost!" ,"\n")    
                        round += 1        
                        break 

                    else:   # Print une erreur si l'input des choix d'attaque retourne une mauvaise valeurs 
                        print(error)

                    break
                


                    
                elif battle_choice == "2" : # we open the inventory 

                    print(f" There is : " + str(player["potion"]) + " potion in your bag")
                    inventory_choice = input ("Make your choice {my_name} \n  1 : Use potion (+15HP) \n  2 : Use maxipotion (+50HP) \n  3 : Back ")

                    if inventory_choice == "1" : # the player chose to use normal potion
                        if player["potion"] > 0 : 
                            player["HP"] = fonction.potion(player["HP"]) # we add hp to the player 
                            player["potion"] -= 1
                            print ( " You feel better.. Now you have : ", player["HP"] ," HP", " and you have :" , player["potion"] , "potion in your bag")
                            diff = player["HP"] 
                            player["HP"] = fonction.enemy_attack(player["HP"]) # we sustract the hp from the player hp after he got attacked
                            print(f"You are under attack!! \n{my_name} : -", diff - player["HP"], "HP lost!" ,"\n")      
                            round += 1        
                            break
                        else: 
                            print("You don't have potion! ")


                    elif inventory_choice == "2" :

                        if player["potion_max"] > 0 :
                            player["HP"] = fonction.max_potion(player["HP"]) # we add hp to the player 
                            player["potion_max"] -= 1
                            print ( " You feel better.. Now you have : ", player["HP"] ," HP", " and you have :" , player["potion"] , "potion in your bag")
                            diff = player["HP"] 
                            player["HP"] = fonction.enemy_attack(player["HP"]) # we sustract the hp from the player hp after he got attacked
                            print(f"You are under attack!! \n{my_name} : -", diff - player["HP"], "HP lost!" ,"\n")  
                            round += 1          
                            break 

                        else:
                            print("You don't have potion_max! !")    



                    elif inventory_choice == "3" : # player chooses to quit inventory
                        break

                    else:
                        print(error)
                        break 
     
                elif battle_choice == "3" : # player chooses to leave the game
                    sys.exit("You leave the game") 
                        
                else:
                    print(error)
                    break 

            dead = 0 
            for j in enemies : # we show which enemy died according to his hp
                if j["HP"] <= 0 :
                    j["HP"] = 0
                    print(j["Name"] , "just died!")
                    dead +=1 

            if dead == len(enemies) : # when all enemies are dead we won the game 
                print ("You won!!")

                if os.path.exists('./data/scores.csv') == False : # check if scores.csv exists, if not create it 

                    header = ["Name", "Score"]

                    with open('./data/scores.csv', 'w') as score_csv: # create scores.csv
                        writer = csv.writer(score_csv, delimiter=',')
                        writer.writerow(header) # write the header

                # Update scores.csv
                with open('./data/scores.csv', 'a', newline='') as score_csv: # add a new line in csv file
                    writer = csv.writer(score_csv, delimiter=',')
                    score_line = [my_name, round]
                    writer.writerow(score_line) # add a line with current name and score
                
                break

            if player["HP"] <= 0 : # when our player have under or 0 hp he loses the game
                print ("Game Over!")
                break
    
    elif menu_choice == '2' : # Player chooses score menu  

        if os.path.exists('./data/scores.csv') == False :
            print("==================================")
            print('Sorry no scores available for now.')
            print("==================================")
            continue

        else :
            print("==================================")
            # Display scores
            with open('./data/scores.csv') as score_csv:
                reader = csv.reader(score_csv, delimiter=',') #reader mode
                for ligne in reader: # read each line
                    if len(ligne) != 0 :
                        print(ligne[0], ' ', ligne[1])
            print("==================================")
            continue

    elif menu_choice == "3" : # the player chose to leave the game
        leave = False 
        break
        
    else: 
        print(error)
        continue
    




                
