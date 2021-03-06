import os
from room import Room
from player import Player
from item import Item

###########################################################
#https://www.geeksforgeeks.org/clear-screen-python/
# Clear the terminal
# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
###########################################################

# # Declare some items
# items = {
#     "rocks": Item("rocks"),
#     "potion": Item("potion"),
#     "sword": Item("sword"),
#     # "torch": Item("torch"),
#     # "gold": Item("gold"),
#     # "junk": Item("junk"),
#     # "pirate booty": Item("all kinds of treasure")
# }


# Add items to rooms


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", [Item("Rocks", "A pile of rocks")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", [Item("Potion", "A magical elixer to enhance your senses")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", [Item("Old_Sword", "It may be of use again like it once was")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasurechamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Something fun!
# https://asciiart.website/index.php?art=objects/computers
# http://patorjk.com/software/taag/#p=display&h=0&f=Fire%20Font-s&t=Welcome!
print("""

                         ___..-.---.---.--..___
               _..-- `.`.   `.  `.  `.      --.._
              /    ___________\\   \\   \\______    \\
              |   |.-----------`.  `.  `.---.|   |
              |`. |'  \\`.        \\   \\   \\  '|   |
              |`. |'   \\ `-._     `.  `.  `.'|   |
             /|   |'    `-._o)\\  /(o\\   \\   \\|   |\\
           .' |   |'  `.     .'  '.  `.  `.  `.  | `.
          /  .|   |'    `.  (_.==._)   \\   \\   \\ |.  \\         _.--.
        .' .' |   |'      _.-======-._  `.  `.  `. `. `.    _.-_.-'\\\\
       /  /   |   |'    .'   |_||_|   `.  \\   \\   \\  \\  \\ .'_.'     ||
      / .'    |`. |'   /_.-'========`-._\\  `.  `-._`._`. \\(.__      :|
     ( '      |`. |'.______________________.'\\      _.) ` )`-._`-._/ /
      \\\\      |   '.------------------------.'`-._-'    //     `-._.'
      _\\\\_    \\    |ARE YA READY TO PLAY`.`.|    '     //
     (_  _)    '-._|________________________|_.-'|   _//_
     /  /      /`-._      |`-._     / /      /   |  (_  _)
   .'   \\     |`-._ `-._   `-._`-._/ /      /    |    \\  \\
  /      `.   |    `-._ `-._   `-._|/      /     |    /   `.
 /  / / /. )  |  `-._  `-._ `-._          /     /   .'      \\
| | | \\ \\|/   |  `-._`-._  `-._ `-._     /     /.  ( .\\ \\ \\  \\
 \\ \\ \\ \\/     |  `-._`-._`-._  `-._ `-._/     /  \\  \\|/ / | | |
  `.\\_\\/       `-._  `-._`-._`-._  `-._/|    /|   \\   \\/ / / /
              /    `-._  `-._`-._`-._  ||   / |    \\   \\/_/.'
            .'         `-._  `-._`-._  ||  /  |     \\
           /           / . `-._  `-._  || /   |      \\
          '\\          / /      `-._    ||/'._.'       \\
           \\`.      .' /           `-._|/              \\
            `.`-._.' .'               \\               .'
              `-.__\\/                 `\\            .' '
                                       \\`.       _.' .'
                                        `.`-._.-' _.'
                                          `-.__.-'

                                                     ____ 
 (  (             (                                 |   / 
 )\\))(   '   (    )\\                  )       (     |  /  
((_)()\\ )   ))\\  ((_)   (     (      (       ))\\    | /   
_(())\\_)() /((_)  _     )\\    )\\     )\\  '  /((_)   |/    
\\ \\((_)/ /(_))   | |   ((_)  ((_)  _((_))  (_))    (      
 \\ \\/\\/ / / -_)  | |  / _|  / _ \\ | '  \\() / -_)   )\\     
  \\_/\\_/  \\___|  |_|  \\__|  \\___/ |_|_|_|  \\___|  ((_)                        
""")

# Make this ... because I can.
line_updn = ("\n˄˅˄˅˄˅˄˅˄˅˄˅˄˅˄˅˄˅˄˅˄˅˄˅˄˅˄˅˄˅˄˅˄˅˄˅˄˅˄˅˄˅˄˅˄˅")



# Make a new player object that is currently in the 'outside' room.
user_name = input(
    "\n\nI've heard rumors there's a new hero in town, we're all happy you're here!\nPlease, what name shall you be known by?\n")
player = Player(user_name, room['outside'])
























# Make try/except for program
try:
    # Write a loop that:
    game_loop = True

    # Print the current room
    print(f"\nYour location: {player.current_room.name} -\n{player.current_room.description}")



    # Main game loop
    while game_loop:

        # Quick sleep, then clear terminal
        sleep(.25)
        clear()
        
        # prints the current room
        print(f"{line_updn}\nYour location: {player.current_room.name}")
        
        # Print item details
        # print(f"Items in location: {player.current_room.name}")
        print("\nItems:")
        print(*[item for item in player.current_room.items], sep=',')

        # * Prints the current room description (the textwrap module might be useful here).
        print(f"\n{player.current_room.description}")

        # Collect input from user
        choice = input(
        """
Where would you like to go? Or what would you like to do?\n
Your choices are:
[n] - North
[s] - South
[e] - East
[w] - West

[drop {item}] - Drop a speciffic item
[get {item}]  - Pick up a specific item\n

[q] - Quit this amazing game
"""
        )

        # If the user enters "q", quit the game.
        if choice.upper() == ('Q'):
            try:
                game_loop = False
            except Exception:
                print("\nSorry pal, you can't go that way right now.\n")

        # North
        # * Waits for user input and decides what to do.
        if choice.upper() == ('N'):
            try:
                player.current_room.n_to.name
                player.current_room = player.current_room.n_to

                # * Prints the current room name
                # print(f"\nYour location: {player.current_room.name}")
            except Exception:
                # If the user enters a cardinal direction, attempt to move to the room there. Print an error message if the movement isn't allowed.
                print(
                    f"\n\n{line_updn}\nSorry, pal, it's impossible to go {choice} right now.\n")

        # South
        # * Waits for user input and decides what to do.
        elif choice.upper() == ('S'):
            try:
                player.current_room.s_to.name
                player.current_room = player.current_room.s_to

                # * Prints the current room name
                # print(f"\nYour location: {player.current_room.name}")
            except Exception:
                # If the user enters a cardinal direction, attempt to move to the room there. Print an error message if the movement isn't allowed.
                print(
                    f"\n\n{line_updn}\nSorry, pal, it's impossible to go {choice} right now.\n")

        # East
        # * Waits for user input and decides what to do.
        elif choice.upper() == ('E'):
            try:
                player.current_room.e_to.name
                player.current_room = player.current_room.e_to

                # * Prints the current room name
                # print(f"\nYour location: {player.current_room.name}")
            except Exception:
                # If the user enters a cardinal direction, attempt to move to the room there. Print an error message if the movement isn't allowed.
                print(
                    f"\n\n{line_updn}\nSorry, pal, it's impossible to go {choice} right now.\n")

        # West
        # * Waits for user input and decides what to do.
        elif choice.upper() == ('W'):
            try:
                player.current_room.w_to.name
                player.current_room = player.current_room.w_to

                # * Prints the current room name
                # print(f"\nYour location: {player.current_room.name}")
            except Exception:
                # If the user enters a cardinal direction, attempt to move to the room there. Print an error message if the movement isn't allowed.
                print(
                    f"\n\n{line_updn}\nSorry, pal, it's impossible to go {choice} right now.\n")

        else:
            print("Please enter a valid key")

# End of the world error!
except Exception:
    print("Something REALLY bad happened! Now what?")
