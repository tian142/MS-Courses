# Welcome to Monster Dance Battle!
from random import choice

# npc means non-playable character, this will be the monster your player monster will be battling
# hp means hit points or how much overall health a monster has
# dance moves from an opposing monster will reduce hit points by the dance score amount

# TODO: write a function that will read the contents of a file containing monster npc info and return a dictionary of that info
# npc_monsters.txt has the format the info will be in
# hint: be sure to convert the hp numbers to ints!
# Example output {Cookie:20, Kelpie:25, Griffin:30}


def get_npc_monster_dictionary(filename):
    file = open(filename)
    monsters = {}
    for line in file:
        name, value = line.split(",")
        monsters[name] = value.strip()  # removes the new line n/
    return monsters


npc_monster_hps = get_npc_monster_dictionary("npc_monsters.txt")

npc_monster_dance_moves = [{"Vogue": 3, "The Moonwalk": 12}, {
    "The Twist": 5, "Sprinkler": 10}, {"Box Step": 4, "Floss": 12}]

# TODO: Write a function that will randomly select a monster&hp from the given dictionary stored in the npc_monster_hps global variable

# This function will return a tuple, the monster name and hp as one tuple
# Example output: (Cookie, 20)


def select_npc_monster():
    # make a list of the object npc... and choice makes arandom choice of the object
    return choice(list(npc_monster_hps.items()))

# TODO: Write a function that will randomly select a dance move set with attack values from the given list stored in the npc_monster_dance_moves global variable
# This function will return a dictionary,the dance moves as the dictionary
# Example output: {"Vogue":3, "The Moonwalk":12}


def select_npc_dance_moves():
    # make a list of the object npc... and choice makes arandom choice of the object
    return choice(npc_monster_dance_moves)
    # randomly chosing form an existing list

# TODO: Write a function that will get the monster name and hp from user input. You will need to limit the user entered hp value to be greater than 1 and less than or equal to 30. Keep prompting until the user enters a number that works.

# This function will return a tuple, the monster name and hp as one tuple
# Example output: (Jess, 20)


def build_player_monster():
    player_monster = input('welcome! please enter a monster name:')
    player_hp = int(input('now, enter your monster hp:'))
    while player_hp < 1 or player_hp > 30:
        player_hp = int(input(
            'Your monster hp must be greater than 1 and less than or equal to 30, try again:'))
    return player_monster, player_hp


# print(build_player_monster())

# TODO: Write a function that will create the player monster dance moves from user input.
# You will need to limit the dance move score to be greater than 1 less than or equal to 15.
# Keep prompting until the user enters a number that works.

# This function will return a dictionary, the dance moves as a dictionary with two dance moves and scores
# get the dance move name as the key
# get the dance move score as the value
# Example output: {"Sprinkler":3, "Lawnmower":12}


def build_player_monster_dance_moves():
    player_monsters = {}
    for i in range(0, 2):
        dance_move = input('pleaser enter a dance move:')
        damage = int(input('please enter damag(between 1 and 15):'))
        while damage < 1 or damage > 15:
            damage = int(input('value must be between 1 and 15'))
        player_monsters[dance_move] = damage
    return player_monsters


def battle(player_monster, player_dance_moves, npc_monster, npc_dance_moves):

    npc_dance_move = choice(list((npc_dance_moves.items())))
    npc_dance_move_name = npc_dance_move[0]
    npc_dance_move_score = npc_dance_move[1]
    print("The opposing master chose:" + npc_dance_move_name +
          "with a score of" + str(npc_dance_move_score))

    player_dance_move_name = input(
        'Please enter the name of the move you want to use: ')

    player_dance_moves_names = player_dance_moves.keys()
    while(player_dance_move_name not in player_dance_moves_names):
        player_dance_move_name = input("please enter correct name")

    player_hp = int(player_monster[1])
    npc_hp = int(npc_monster[1])

    player_dance_move_score = player_dance_moves[player_dance_move_name]

    player_hp = player_hp - int(npc_dance_move_score)
    npc_hp = npc_hp - int(player_dance_move_score)

    print("Player HP: " + str(player_hp))
    print("NPC HP: " + str(npc_hp))
    # TODO: return the player name and the new hp as a tuple and the npc player name and the new hp as a tuple
    # hint remember tuples are immutable
    # hint you can return multiple values in Python by separating them by a comma after the return keyword
    return(player_monster[0], player_hp), (npc_monster[0], npc_hp)

# print(battle(build_player_monster(), build_player_monster_dance_moves(),
#              select_npc_monster(), select_npc_dance_moves()))


# TODO: Finish this function that will use a loop to run the game
# this function doesn't return anything


def run_dance_battle():
    # TODO: call the build_player_monster() function and store the result in a variable
    player_monster = build_player_monster()
    # TODO: call the build_player_monster_dance_moves() function and store the result in a variable
    player_monster_dance_moves = build_player_monster_dance_moves()
    # TODO: call the select_npc_monster() function and store the result in a variable
    npc_monster = select_npc_monster()
    # TODO: call the select_npc_dance_moves() function and store the result in a variable
    npc_monster_dance_moves = select_npc_dance_moves()
    # # TODO: finish this while loop condition to keep taking turns until either the npc or the player is at 0
    player_hp = int(player_monster[1])
    npc_hp = int(npc_monster[1])
    while player_hp > 0 and npc_hp > 0:
        player_monster, npc_monster = battle(
            player_monster, player_monster_dance_moves, npc_monster, npc_monster_dance_moves)
        player_hp = int(player_monster[1])
        npc_hp = int(npc_monster[1])
    if player_hp <= 0:
        print('npc has won!')
    else:
        print('player won!')
    # TODO: use a conditional statement to print who won!

    # TODO: write two simple automated tests to test the functions you wrote


run_dance_battle()
