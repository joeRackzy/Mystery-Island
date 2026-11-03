
import time
import random


# 1. DISPLAY TITLE
def display_title():
    print("\n\t🧗 MYSTERY ISLAND 🌊🏝️")
    print("The Lost Lighthouse")

    print("\nLoading", end="")

    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(1)

    print("\n")


# 2. DISPLAY INSTRUCTIONS
def display_instructions():
    print("\nYOUR MISSION:")
    print("1. You are stranded on a mysterious island.")
    print("2. Find the rope and lantern.")
    print("3. Use the rope to cross the old bridge.")
    print("4. Use the lantern to restore the lighthouse.")
    print("5. You have only 5 energy points.")
    print("6. Rain prevents you from moving.")
    print("7. Make wise decisions to survive.\n")


# 3. GET PLAYER NAME
def get_player_name():
    while True:
        name = input("Enter your name: ").strip()

        if name == "":
            print("Name cannot be empty.")
            continue

        return name


# 4. CREATE PLAYER
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


# 5. UPDATE WEATHER
def update_weather(player):
    player["temperature"] = random.randint(10, 25)

    if player["temperature"] > 15:
        player["raining"] = False
    else:
        player["raining"] = True


# 6. DISPLAY WEATHER
def display_weather(player):
    print(f"\nTemperature: {player['temperature']}°C")

    if player["raining"]:
        print("🌧️ It is raining! You cannot move.")
    else:
        print("☀️ The weather is clear.")


# 7. DISPLAY PLAYER STATUS
def display_status(player):
    print("\n========== PLAYER STATUS ==========")
    print(f"Name: {player['name']}")
    print(f"Energy: {player['energy']}")
    print(f"Location: {player['location']}")
    print(f"Inventory: {player['inventory']}")
    print("===================================")


# 8. ISLAND MAP
def get_available_locations(location):
    island_map = {
        "Beach": ["Jungle"],
        "Jungle": ["Beach", "Cave"],
        "Cave": ["Jungle", "Old Bridge"],
        "Old Bridge": ["Cave", "Lighthouse"],
        "Lighthouse": ["Old Bridge"]
    }

    return island_map[location]


# 9. MOVE PLAYER
def move_player(player):
    if player["raining"]:
        print("You cannot move while it is raining.")
        return

    available_locations = get_available_locations(
        player["location"]
    )

    print("\nWhere would you like to go?")

    for number, location in enumerate(available_locations, 1):
        print(f"{number}. {location}")

    print("0. Cancel")

    choice = input("Choose a location: ").strip()

    if choice == "0":
        return

    try:
        choice = int(choice)

        if choice < 1 or choice > len(available_locations):
            print("Invalid choice.")
            return

    except ValueError:
        print("Please enter a number.")
        return

    destination = available_locations[choice - 1]

    if destination == "Old Bridge" and "Rope" not in player["inventory"]:
        print("You need a rope to reach the Old Bridge.")
        return

    if destination == "Lighthouse" and "Rope" not in player["inventory"]:
        print("You need a rope to cross the bridge.")
        return

    player["location"] = destination
    player["energy"] -= 1

    print(f"You moved to {destination}.")

    if player["energy"] <= 0:
        player["energy"] = 0
        print("🪫 You have run out of energy!")


# 10. COLLECT OBJECTS
def collect_object(player):
    objects = {
        "Jungle": "Rope",
        "Cave": "Lantern"
    }

    location = player["location"]

    if location not in objects:
        print("There is nothing useful to collect here.")
        return

    item = objects[location]

    if item in player["inventory"]:
        print(f"You already collected the {item}.")
        return

    print(f"\nYou found a {item}!")

    choice = input(
        "Do you want to collect it? (yes/no): "
    ).strip().lower()

    if choice == "yes":
        player["inventory"].append(item)
        print(f"{item} added to your inventory.")
    else:
        print("You decided to leave it behind.")


# 11. RESTORE LIGHTHOUSE
def restore_lighthouse(player):
    if player["location"] != "Lighthouse":
        print("You must be at the Lighthouse first.")
        return False

    if "Lantern" not in player["inventory"]:
        print("You need a lantern to restore the beacon.")
        return False

    print("\nYou found the lighthouse beacon!")

    choice = input(
        "Restore the beacon? (yes/no): "
    ).strip().lower()

    if choice == "yes":
        print("\n🎉 THE LIGHTHOUSE IS RESTORED!")
        print("🏆 YOU HAVE WON MYSTERY ISLAND!")
        return True

    print("You decided not to restore it yet.")
    return False


# 12. PLAY GAME
def play_game():
    display_title()
    display_instructions()

    player_name = get_player_name()
    player = create_player(player_name)

    print(f"\nWelcome, {player['name']}!")
    print("Your adventure begins at the Beach.")

    while True:
        if player["energy"] <= 0:
            print("\n💀 GAME OVER! You lost all your energy.")
            break

        update_weather(player)
        display_weather(player)

        print("\n========== GAME MENU ==========")
        print("1. Move")
        print("2. Collect object")
        print("3. View status")
        print("4. Restore lighthouse")
        print("5. Quit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            move_player(player)

        elif choice == "2":
            collect_object(player)

        elif choice == "3":
            display_status(player)

        elif choice == "4":
            if restore_lighthouse(player):
                break

        elif choice == "5":
            print("You decided to leave the island.")
            break

        else:
            print("Invalid choice. Please try again.")


# 13. REPLAY GAME
def main():
    while True:
        play_game()

        replay = input(
            "\nWould you like to play again? (yes/no): "
        ).strip().lower()

        if replay != "yes":
            print("\nThank you for playing Mystery Island!")
            break


if __name__ == "__main__":
    main()
