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