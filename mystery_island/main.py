import time
def display_tittle():
    print("\n\t 🧗 MYSTERY ISLAND 🌊🏝️".upper())

    
    print("\nLoading completed", end="")
    
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(1)
    

def display_instruction():
  
    print("\n\nYour mission and rules".upper())

    print("\n1. You are stranded on a mysterious island.")
    print("2. Your mission is to restore the lighthouse beacon.")
    print("3. Explore five locations to find useful objects.")
    print("4. You have only 5 energy points.")
    print("5. Watch out for rain because you cannot move while it is raining.")
    print("6. Find the rope to cross the old bridge.")
    print("7. Find the lantern to restore the lighthouse.")    
                 
    
def get_player_name():
    while True:
        name = input("\nwhat is you name ").strip()
        if name == "":
            print("Name cannot be empty try again")
            continue
        return name 

def create_player(name):
    player = {
        "name": name,
        "energy": 5,
        "location": "Beach",
        "inventory": [],
        "temperature": 20,
        "raining": False
    }

    return player    

def update_weather(player):
    if player["temterature"] >15:
        player["raining"] = False
    else:
        player["raining"]= True    

def main():
    display_tittle()
    display_instruction()
    player_name = get_player_name()
    player = create_player(player_name)
    print(f"You are welcome {player["name"]}")
    print(f"Energy: {player["energy"]}")
    print(f"Location: {player["location"]}")
    print(f"Inventory: {player["inventory"]}")
    print(f"temperature: {player["temperature"]}")
    print(f"Raining: {player["raining"]}")
    

main()
if __file__ == "__main__":    


   main()