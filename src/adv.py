from room import Room
from player import Player


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

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

# Make a new player object that is currently in the 'outside' room.
user_name = input("\n\nI've heard rumors there's a new hero in town, we're all happy you're here!\nPlease, what name shall you be known by?\n")
player = Player(user_name, room['outside'])

# Make try/except for program
try:
    # Write a loop that:
    game_loop = True

    # Print the current room
    print(f"\nYou are {player.current_room.name} {player.current_room.description}")

    # Main game loop
    while game_loop:

        # Collect input from user
        choice = input("User Input: ")

        # If the user enters "q", quit the game.
        if choice.upper() == ('Q'):
            try:
                game_loop = False
            except Exception:
                print("\nSorry pal, you can't go that way right now.\n")

        # North
        if choice.upper() == ('N'):
            try:
                player.current_room.n_to.name
                player.current_room = player.current_room.n_to
                print(f"Current room name: {player.current_room}")
            except Exception:
                print("\nSorry, pal, it's impossible to go {choice} right now.\n")

        # South
        elif choice.upper() == ('S'):
            try:
                player.current_room.s_to.name
                player.current_room = player.current_room.s_to
                print(f"Current room name: {player.current_room}")                    
            except Exception:
                print("\nSorry, pal, it's impossible to go {choice} right now.\n")

        # East
        elif choice.upper() == ('E'):
            try:
                player.current_room.e_to.name
                player.current_room = player.current_room.e_to
                print(f"Current room name: {player.current_room}")
            except Exception:
                print("\nSorry, pal, it's impossible to go {choice} right now.\n")

        # West
        elif choice.upper() == ('W'):
            try:
                player.current_room.w_to.name
                player.current_room = player.current_room.w_to
                print(f"Current room name: {player.current_room}")
            except Exception:
                print("\nSorry, pal, it's impossible to go {choice} right now.\n")

        else:
            print("Please enter a valid key")

        # * Prints the current room name
        print(f"Current room name: {choice}")

        # End of the world error!
except Exception:
    print("Something bad happened! Now what?")

    # * Prints the current description (the textwrap module might be useful here).

    # * Waits for user input and decides what to do.

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.

