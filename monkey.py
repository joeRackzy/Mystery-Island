import random
import time

def display_wlcome():
    print("\n======@gamer======")
    print("\n\tloading", end="")
    for tim in range(5):
        print(".", end="",flush=True)
        time.sleep(1)
    print("\n..WELCOME TO MYSTERY ISLAND...")

def display_instructions():
    print("\nYOUR MISSION:")
    print("1. You are stranded on a mysterious island.")
    print("2. Find the rope and lantern.")
    print("3. Use the rope to cross the old bridge.")
    print("4. Use the lantern to restore the lighthouse.") 
    print("5. You have only 5 energy points.")
    print("6. Rain prevents you from moving.")
    print("7. Make wise decisions to survive.\n") 

def create_player():
    while True:
            name = input("what is your name: ").strip()  
            if name == "":
                print("Name mush not be empty")
                continue
            
            player = {
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

    collect_object(player)
   




            
