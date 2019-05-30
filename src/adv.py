from room import Room
from player import Player
from item import Item
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

item ={
    "Ak47":  Item("Ak47", "Deadly Weapon, Stay out of it."),
    "Sheild": Item("Sheild", "Almost same as Captain America Sheild, Heavy but worth it."),

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
room["outside"].items = [item["Ak47"], item["Sheild"]]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

name = input("Please Enter Your name : ")
player = Player(name, room["outside"])
game_over = False

def room_info(char)
    print(f"{char.name}, {char.room}\n")
    if char.room.items== []:
        print("This room holds no items.\n")
    elif len(char.room.items) == 2:
        print(f"This room holds a {char.room.items[0].name} and a {char.room.items[1].name}.\n")
    else:
        print(f"This room holds a {char.room.items[0].name}.\n")

playerAction = " "
nextRoom = " "

print ("Enter Your Movement, Press [N] for North, [S] for South, [E] for East, [W] for West and [q] Quit")
while True :
    try:
        playerAction = input("------> ")
        if playerAction == "Q" or playerAction == "q":
            break
        elif playerAction == "N" or playerAction == "n":
            player.room =  player.move_room.n_to
        elif playerAction == "E" or playerAction == "e":
            player.room =  player.room.e_to
        elif playerAction == "S" or playerAction == "s":
            player.room = player.room.s_to
        elif playerAction == "W" or playerAction == "w":
            player.room = player.room.w_to
        else: 
            print('Incorrect input. Please use N, S, E, or W')
    except AttributeError:
            print('You Can not go this way.')
            playerAction = input("----->")

