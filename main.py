def printStatus(player):
    for key, value in player.items():
        print(f"{key.capitalize()}: {'(' if key == "name" else ''}{value}{')' if key == "name" else ''}")

def dodge(player):
    print(f"{player['name']} uses 10 energy to dodge.")
    player["energy"] -= 10

def daggerSlash(player, opponent, dodged):
    print(f"{player['name']} uses 6 energy.")
    player["energy"] -= 6

    if dodged:
        dodge(opponent)
    
    print(f"{opponent['name']} received {'no' if dodged else '10'} damage.")
    opponent["health"] -= 10 if not dodged else 0

def vampiricClaws(player, opponent, dodged):
    print(f"{player['name']} uses 25 energy.")
    player["energy"] -= 25

    if dodged:
        dodge(opponent)
    
    print(f"{opponent['name']} received {'no' if dodged else '40'} damage.")
    opponent["health"] -= 40 if not dodged else 0

def drainLife(player, opponent, dodged):
    print(f"{player['name']} uses 13 energy.")
    player["energy"] -= 13

    if dodged:
        dodge(opponent)

    print(f"{opponent['name']} received {'no' if dodged else '6'} damage.")

    if not dodged:
        print(f"{player['name']} gains 10 health.")
        opponent["health"] -= 6
        player["health"] += 10

def moveEffects(playerMove, opponentMove, player, opponent):
    if playerMove.lower() == "a":
        daggerSlash(player, opponent, opponentMove.lower() == "c")
    elif playerMove.lower() == "b":
        vampiricClaws(player, opponent, opponentMove.lower() == "c")
    elif playerMove.lower() == "d":
        drainLife(player, opponent, opponentMove.lower() == "c")
    elif playerMove.lower() == "e":
        print(f"{player['name']} does nothing.")

#Main
print("Welcome Vampire Spawn!")
print("Fight for the right to ascend into a Vampire lord")
print("Attempt to knockout your opponent.")
print("Use your vampiric moves to outsmart your opponent.")

print("\nPlayers enter your names...")

player1 = {
    "name": input("Player 1: "),
    "health": 100,
    "energy": 50,
}

player2 = {
    "name": input("Player 2: "),
    "health": 100,
    "energy": 50,
}

print(f"\nLet the duel between {player1["name"]} and {player2["name"]} begin!")

night = 1
while(player1["health"] > 0 and player2["health"] > 0):
    print(f"=== Night {night} ===\n==========")
    print("Player Status\n----------")
    printStatus(player1); print("----------")
    printStatus(player2); print("==========")

    print("\nAvailable Moves:" \
    "\nA. Dagger Slash (10 damage; energy: 6)" \
    "\nB. Vampiric Claws (40 damage; energy: 25)" \
    "\nC. Dodge: Bat Form (nullifies incoming attack; energy: 10)" \
    "\nD. Drain Life (deals 6 damage then heals self by 10; energy: 13)" \
    "\nE. Do nothing (energy: 0)\n")

    player1Move = input(f"Player 1 ({player1["name"]}), choose your move: ")
    player2Move = input(f"Player 2 ({player2["name"]}), choose your move: ")

    print("\nMove Effects:")
    moveEffects(player1Move, player2Move, player1, player2)
    moveEffects(player2Move, player1Move, player2, player1)

    input("\n\nPress Enter to continue...")
    night += 1

#not done yet
#things to add:
#rest per 3 nights
#winner announcement
#update text prompts