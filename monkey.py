import random
import time

from pathlib import Path
JSON_FILE = Path(__file__).resolve().parent / "monkey.json"
import json


def display_welcome():
    print("\n======@gamer======")
    print("\n\tloading", end="")
    for tim in range(5):
        print(".", end="",flush=True)
        time.sleep(1)
    print("\n..WELCOME TO MYSTERY ISLAND...")

def display_instructions():
    print("\nYOUR MISSION:")
    for i in range(1):
            
        print("\n1. You are stranded on a mysterious island.",end="",flush=True)
        time.sleep(2)
        print("\n2. Find the rope and lantern.")
        time.sleep(2)
        print("3. Use the rope to cross the old bridge.",end="",flush=True)
        time.sleep(2)
        print("\n4. Use the lantern to restore the lighthouse.",end="",flush=True) 
        time.sleep(2)
        print("\n5. You have only 5 energy points.",end="",flush=True)
        time.sleep(2)
        print("\n6. Rain prevents you from moving.",end="",flush=True)
        time.sleep(2)
        print("\n7. Make wise decisions to survive.\n",end="",flush=True)
        time.sleep(3) 

def create_player():
    while True:
            name = input("what is your name: ").strip()  
            if name == "":
                print("Name mush not be empty")
                continue
            
            player = {
                "player_ID": f"player.: {str(count).zfill(3)}".upper(),
                "name": name,
                "location": "beach",
                "inventory": [],
                "energy": 5,
                "temperature": 20,
                "raining": False
            }
            return player    

def update_weather(player):
    
    player["temperature"] = random.randint(10,25)

    if player["temperature"] > 15:
        player["raining"] = False
    else:
        player["raining"] = True    

def display_weather(player):
    print(f"\nTemperature:{player["temperature"]}°C")

    if player["raining"]:
        print("🌧️it raining, you cannot move") 
    else:
        print("☀️ The weather is clear.")

def display_status(player):
    print("="*5,"DISPLAY.STATUS","="*5)
    print(f"\nPlayer Ticket: {player["player_ID"]}")
    print(f"Name: {player["name"]}")
    print(f"Location: {player["location"]}")
    print(f"Energy: {player["energy"]}")
    print(f"Inventory: {player["inventory"]}")
    print("="*25)


def get_avaliable_location(location):
    island_map = {
        "beach": ["jungle"],
        "jungle": ["beach","cave"],
        "cave": ["jungle", "old_bridge"],
        "old_bridge": ["cave", "lighthouse"],
        "lighthouse": ["old_bridge"]
    }
    return island_map[location]

def move_player(player):
    if player["raining"]:
        print("please you cannot move is raining")
        return
    avaliable_locations = get_avaliable_location(player["location"])

    for number , location in enumerate(avaliable_locations, 1):
        print(f"{number}. {location}")

    choice = input("choose a location!")
    if choice == "":
        return
    try:
        choice = int(choice)
        if choice < 1 or choice > len(avaliable_locations):
            raise ValueError 
    except ValueError:
        print("invalid choice please try again ")
        return
    destination = avaliable_locations[choice - 1]

    if destination == "old_bridge" and "rope" not in player["inventory"]:
        print("You  need a rope to get to old bridge.")  
        return 
    
    player["location"] = destination
    player["energy"] -= 1
    if player["energy"] <=0:
        print("GAME OVER! You have run out of energy.") 
        return
    
    print(f"You have move to {destination}")

    
def collect_object(player):
    if player["location"] not in "jungle" and player["location"] not in "cave":
        print(f"You have nothing to collect in {player["location"]}")
        return 

    if player["location"] == "jungle" and "rope" not in player["inventory"]:
        answer = input("You found a rope! do you like to collet (yes/no) ").strip().lower()

        if answer == "yes":
            player["inventory"].append("rope")
            print("You have move rope to inventory")
        elif answer == "no":
            print("you left the rope there!")
        else:
            print("invalid input try again")
            return


    elif player["location"] == "cave" and "lantern" not in player["inventory"]:
        answer = input("You found a lantern! do you like to collect it (yes/no)")

        if answer == "yes":
            player["inventory"].append("lantern")
            print("You have move lantern to inventory")
        elif answer == "no":
            print("you left the lantern there")
        else:
            print("invalid input try again")
            return    

def restore_lighthouse(player):
    if player["location"] != "lighthouse":
        print("you must get to lighthouse before you can retsore the beacon")
        return
    if "lantern" not in player["inventory"]:
        print("there is not lanter in you inventory!")
        print("you must have the lantern in your inventory")
        return

    choice = input("do you want to restore the beacon?").lower().strip()
    if choice == "yes":
        print("You have restore the beacon".upper())
        return True

    elif choice == "no":
        print("You decided not to retsore the it no ")
        return False              
    else:
        print("invalid input try again")
        return False
tickets = []
count = 1    
def player_id(player):
    global count
    playing_ticket = player["player_ID"]
    count += 1
    print(f"\n{playing_ticket}")

def load_player_ticket():

    if not JSON_FILE.exists():
        return []
    try:
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return [] 

def ticket(player):
   ticket = {
       "ID": player["player_ID"],
       "Name": player["name"],
       "last energy": player["energy"]
       }
   return ticket       
    
def save_player_ticket(ticket):

    tickets = load_player_ticket()
    tickets.append(ticket)

    with open(JSON_FILE, "w") as file:
        json.dump(tickets, file, indent=4)

 
def play_game():
    
    display_welcome()
    player =create_player()
    display_instructions()
    player_id(player)
    print("\nyour live location is currently in beach\n".title())
    
    while True:
        update_weather(player)
        display_weather(player)
        print("===== menu=====".upper())
        print("\n1. Move")
        print("2. Collect object")
        print("3. Display status")
        print("4. Restore lighthouse")
        print("5. Save player result")
        print("6. Load players results")
        print("7. Quit")
        choice = input("Choose an option: ")
        if choice == "":
            print("choose from 1-5")
            continue
        try:
            choice = int(choice)
            if choice < 1 or choice > 7:
                raise ValueError
        except ValueError:
            print("please enter a number. ")
            continue    
        if choice == 7:
            print("goodbye see you again")
            break
        elif choice == 1:
            move_player(player)
        elif choice == 2:
            collect_object(player)
        elif choice == 3:
            display_status(player)
        elif choice == 5:
            if player["location"] == "lighthouse" and "rope" in player["inventory"] and "lantern" in player["inventory"]:
               tick = ticket(player)
               save_player_ticket(tick)
            else:
                print(" you have not finish the game fine and try again")
                continue   
        elif choice == 6:
            lists = load_player_ticket()
            print(lists)      
        if player["energy"] < 3:
            print("\n\t\tWARINING! you are running out of energy".upper())

        if player["energy"] <= 0:
            print("GAME OVER! You have run out of energy.")
            break 
        elif choice == 4:
            won = restore_lighthouse(player)
            if won:
                break

      
def main():
    while True:
        
        play_game()                                        
        replay = input("would you like to play again? (yes/no) ").lower().strip()
        if replay == "yes":
            continue 
                               
        elif replay == "no":
            break
        else:
            continue
                
             

main()

   