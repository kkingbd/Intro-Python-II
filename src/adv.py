from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

currentRoom = room["outside"]

name = input("Please Enter Your name : ")
player = Player(name, currentRoom)

describe = f"{player.name}, {currentRoom}"

playerAction = " "
nextRoom = " "
print ("Enter Your Movement, Press [N] for North, [S] for South, [E] for East, [W] for West and [q] Quit")
while True :
    try:
        playerAction = input("Enter your Movement: ")
        if playerAction == "Q" or playerAction == "q":
            break
        elif playerAction == "N" or playerAction == "n":
            nextRoom =  currentRoom.n_to
            print(nextRoom)
        elif playerAction == "E" or playerAction == "e":
            nextRoom =  currentRoom.e_to
            print(nextRoom)
        elif playerAction == "S" or playerAction == "s":
            nextRoom = currentRoom.s_to
            print(nextRoom)
        elif playerAction == "W" or playerAction == "w":
            nextRoom = currentRoom.w_to
            print(nextRoom)
    except AttributeError:
            print('You Can not go this way.')
            currentRoom = room["outside"]
            playerAction = input("Enter Your Movement, Press [N] for North, [S] for South, [E] for East, [W] for West and [q] Quit\n")
                    
    if  nextRoom :
        currentRoom = nextRoom
    else: 
        print('Incorrect input. Please use N, S, E, or W')
        playerAction = input("Enter Your Movement, Press [N] for North, [S] for South, [E] for East, [W] for West and [q] Quit\n")

