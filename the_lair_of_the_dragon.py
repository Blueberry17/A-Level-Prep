import pickle
from map_data import map_data
from inventory_data import inventory_uses
from colorama import Fore, Style


def pickle_write(game_data_dict):
    """Method to save the game data"""
    try:
        file = open("users_data.pkl", "wb")
        pickle.dump(game_data_dict, file)
        file.close()

    except PermissionError as error:
        print("Could not open file for writing:", error)

    except OSError as error:
        print("Cannot open file:", error)


def pickle_read():
    """Method to read the game data"""
    try:
        file = open("users_data.pkl", "rb")
        game_data_dict = pickle.load(file)
        return game_data_dict

    except OSError as error:
        print("Cannot open file:", error)


def auto_save():
    """Auto-saves the user's data after each decision by the user in-game"""
    pickle_write(game_data)


def divider():
    """A divider to split up text to make the game more readable"""
    print(Style.BRIGHT +
          "\n================================================================================\n" + Style.RESET_ALL)


def bold_text(text):
    """A function to make text bold"""
    return Style.BRIGHT + str(text) + Style.RESET_ALL


def sign_up():
    """A function that creates a new account for a user"""
    verified = False
    username = ""

    while not verified:
        print(f"\nEnter your new {bold_text('username')} (or enter '{bold_text('log in')}').")
        username = input(" >>> ").lower()

        if username == "log in":
            # Redirects the user back to the log-in function
            return None

        elif username in game_data:
            print(Fore.RED + "Sorry, this username is already taken. Please try another." + Fore.RESET)

        elif " " in username:
            print(Fore.RED + "Sorry, your username must not contain any whitespace." + Fore.RESET)

        elif len(username) < 3 or len(username) > 20:
            print(Fore.RED + "Sorry, your username must be more than 3 characters long" + Fore.RESET)

        else:
            # Confirms the user's choice
            print(f"\nAre you sure you want your new username to be '{bold_text(username)}'",
                  f"({bold_text('y/n')})?")
            confirm = input(" >>> ")
            if confirm.lower() == "y":
                print(Fore.LIGHTGREEN_EX + f"\nUsername accepted. Welcome {bold_text(username)}" + Fore.LIGHTGREEN_EX +
                      "!" + Fore.RESET)
                divider()
                print_help()
                verified = True

    # Creates a new dictionary for the user, initialising their values
    user_data = {"high score": 0, "location": 0, "states": {}, "inventory": [], "gold": 0}
    game_data[username] = user_data
    auto_save()

    return user_data


def log_in():
    """A function that logs the user in, or diverts them to the sign-up function"""
    divider()
    print(Style.BRIGHT + "======================")
    print("THE LAIR OF THE DRAGON")
    print("======================")
    print("\nLog in:")

    user_data = None
    while user_data is None:
        print(Style.RESET_ALL + f"\nEnter your {bold_text('username')} (or enter '{bold_text('sign up')}').")
        username = input(" >>> ").lower()

        if username == "sign up":
            # Diverts the user to the sign-up function
            user_data = sign_up()
            game_choice = "new"

        elif username in game_data:
            # Searches through the pre-existing usernames
            user_data = game_data[username]
            high_score = user_data["high score"]
            print(f"\nWelcome back {bold_text(username)}!")
            print(f"Your high score: {bold_text(high_score)}.")
            divider()
            if user_data["location"] <= 0:
                game_choice = "new"
            else:
                game_choice = "open"

        else:
            print(Fore.RED + "Unrecognised username." + Fore.RESET)

    # noinspection PyUnboundLocalVariable
    return user_data, game_choice


def start_game(choice):
    """Determines whether the user is continuing the current game or starting afresh"""
    global user_data

    if choice == "open":
        print("\nEnter the number of your choice.")
        print(" - (1): Start a new game.")
        print(" - (2): Continue your current game.\n")

        while True:
            choice = input(" >>> ")
            if choice == "h" or choice == "help":
                print()
                print_help()
            elif choice == "1" or choice == "2":
                break

    if choice == "1":
        user_data = {"high score": 0, "location": 0, "states": {}, "inventory": [], "gold": 0}
        return 0

    else:
        return user_data["location"]


def print_text(text):
    """A subroutine that prints text with automatic line breaks and with colours for readability"""

    paras = text.split("\n\n")
    max_line_length = 80

    for para in paras:
        current_line_length = 0
        words = para.split()
        for word in words:
            if current_line_length + len(word) + 1 <= max_line_length:
                current_line_length += len(word) + 1
            else:
                print()
                current_line_length = len(word) + 1
            print(word, end=' ')
        print("\n")


def print_inventory():
    print(bold_text('\nYour inventory:'))
    print(f" - {Fore.YELLOW + 'Gold pieces' + Fore.RESET}: {user_data['gold']}")
    for item in user_data["inventory"]:
        if item == "emerald":
            print(f" - {Fore.LIGHTGREEN_EX}Emerald{Fore.RESET}")
        elif item == "ruby":
            print(f" - {Fore.LIGHTRED_EX}Ruby{Fore.RESET}")
        elif item == "diamond":
            print(f" - {Fore.LIGHTBLUE_EX}Diamond{Fore.RESET}")
        else:
            print(f" - {item.capitalize()}")
    print()


def use_inventory(item):
    """Displays the user's inventory"""
    current_item = inventory_uses[item]

    if location in current_item:
        current_use = current_item[location]
        desc = current_use[0]
        next_location = current_use[1]
        items = current_use[2]
        gold = current_use[3]
        state = current_use[4]

        divider()
        print_text(desc)
        for item in items:
            if item not in user_data["inventory"]:
                user_data["inventory"].append(item)
        user_data["gold"] += gold

        print(f"Press {bold_text('return')} to continue.")
        while True:
            choice = input(" >>> ").lower()
            if choice == "i" or choice == "inv" or choice == "inventory":
                print_inventory()
            elif choice == "h" or choice == "help":
                print()
                print_help()
            else:
                break

        if len(current_use) == 7:
            user_data["states"][current_use[5]] = current_use[6]
        user_data["states"][location] = state
        auto_save()

        return next_location

    else:
        # Return False if the item cannot be used
        print(f"Your {item} has no use here.\n")
        return False


def use_gold(required):
    """A function for when the user attempts to spend gold in-game"""
    if user_data["gold"] >= required:
        user_data["gold"] -= required
        return True
    else:
        print("You do not have enough gold to do this.\n")
        return False


def print_help():
    """Displays help to the user"""
    print(bold_text('Instructions:'))
    print(f" - Type '{bold_text('inventory')}' or '{bold_text('i')}' at any point view a list of your items.")
    print(f" - Type '{bold_text('use <item>')}' at any point to attempt to use an item in your",
          "inventory.\n")


def run_game(location):
    """Runs a situation in the game, specified by 'location'"""

    current_data = map_data[location]
    descs = current_data[0]
    options_desc = current_data[1]
    options = current_data[2]
    items = current_data[3]
    gold = current_data[4]
    states = current_data[5]
    desc_valid = current_data[6]

    if location in user_data["states"]:
        if len(current_data) == 8 and desc_valid:
            # Gives the user no choices if they re-encounter the same situation that still has a valid description
            options = [current_data[7]]
            # Keep the current state the same
            states[0] = user_data["states"][location]
        elif len(current_data) == 8:
            # Immediately go to a new situation because the user cannot re-encounter the same situation
            return current_data[7], True
        # Output a different description if the user has already encountered the initial situation
        state = user_data["states"][location]
        desc = descs[state]
    else:
        desc = descs[0]
    print_text(desc)

    for item in items:
        if item not in user_data["inventory"]:
            user_data["inventory"].append(item)
    user_data["gold"] += gold

    # If the situation has no choices or the situation has previously been visited and cannot be visited again
    if len(options) == 1 or (location in user_data["states"] and user_data["states"][location] != 0 and not desc_valid):
        print(f"Press {bold_text('return')} to continue.")

        while True:
            choice = input(" >>> ").lower()
            if choice == "i" or choice == "inv" or choice == "inventory":
                print_inventory()
            elif choice[:3] == "use":
                print("You cannot use items here.\n")
            elif choice == "h" or choice == "help":
                print()
                print_help()
            elif choice == "q" or choice == "quit" or choice == "exit":
                return -3, False
            else:
                break
        user_data["states"][location] = states[0]

        auto_save()
        return options[0], False

    # If the situation has multiple choices
    else:
        print(f"Enter the {bold_text('number')} of your choice.")
        for option in range(len(options)):
            print(f" - ({bold_text(option+1)}) {options_desc[option]}.")
        print()

        while True:
            choice = input(" >>> ").lower()
            if choice == "i" or choice == "inv" or choice == "inventory":
                print_inventory()

            elif choice[:3] == "use":
                if choice[4:] in user_data["inventory"]:
                    choice = use_inventory(choice[4:])
                    # Make sure that the item can be used
                    if choice is not False:
                        auto_save()
                        break
                elif len(choice) == 3:
                    print("Please also enter what you would like to use (use <item>).\n")
                else:
                    print("You do not have this item in your inventory.\n")

            elif choice == "h" or choice == "help":
                print()
                print_help()

            elif choice == "q" or choice == "quit" or choice == "exit":
                return -3, False

            elif choice.isnumeric():
                choice = int(choice)-1
                if 0 <= choice < len(options):
                    if isinstance(options[choice], int):
                        # Normal choices
                        user_data["states"][location] = states[choice]
                        auto_save()
                        choice = options[choice]
                        break
                    else:
                        # Choices that involve the user attempting to use gold
                        choice_parts = options[choice].split("g")
                        required = int(choice_parts[1])
                        if use_gold(required):
                            user_data["states"][location] = states[choice]
                            auto_save()
                            choice = int(choice_parts[0])
                            break

        return choice, False


if __name__ == "__main__":
    game_data = pickle_read()
    game_data["b"] = {"high score": 0, "location": 32, "states": {}, "inventory": ["lantern", "garlic", "ruby", "diamond", "emerald", "magic sword", "healing potion"], "gold": 14}
    user_data, game_choice = log_in()
    play = "y"

    print(f"Enter '{bold_text('h')}' at any point to view help.")

    while play.lower() != "n":
        if game_choice == "open":
            # Carries on where the user left off
            location = start_game(game_choice)
        else:
            print("\nPress return to begin your game.")
            while True:
                choice = input(" >>> ")
                if choice == "h" or choice == "help":
                    print()
                    print_help()
                else:
                    break
            # Starts from the beginning
            location = 0

        divider()

        # '-1' corresponds to death, '-2' corresponds to a win
        while location >= 0:
            location, reroute = run_game(location)
            user_data["location"] = location
            auto_save()
            # Do not output a split if no text has been outputted and the game is simply re-routing
            if not reroute:
                divider()

        if location == -1:
            print("GAME OVER, you lose. You have failed the people of Fallkirk and the many other")
            print("towns destined to fall to the dragon.")

        elif location == -2:
            print("GAME OVER, you win! The people of Fallkirk will forever be in your favour,")
            print("beginning with a huge feast!")

        print("Would you like to start again (y/n)?")
        play = input(" >>> ")

    print("\nThanks for playing!")
