def printStatus(player):
    for key, value in player.items():
        if key == 'name':
            print(f"{key.capitalize()}: ({value})")
        else:
            print(f"{key.capitalize()}: {value}")

#return energy cost, damage, heal
def dodge():
    return 10 

def daggerSlash():
    return 6, 10 

def vampiricClaws():
    return 25, 40

def drainLife():
    return 13, 6, 10

def applyEffects(attacker, target, attackerMove, targetMove, energyVal, damageVal, healVal):
    print(f"{attacker['name']} uses {energyVal} energy."); attacker['energy'] -= energyVal

    if targetMove == "c":
        print(f"{target['name']} uses {dodge()} energy to dodge and receives no damage"); target['energy'] -= dodge()
        return
    
    print(f"{target['name']} received {damageVal} damage"); target['health'] -= damageVal

    if attackerMove == "c":
        print(f"{attacker['name']} gains {healVal} health"); attacker['health'] += healVal


def moveEffects(attackerMove, targetMove, attacker, target):
    if attackerMove == "a":
        applyEffects(attacker, target, attackerMove, targetMove, *daggerSlash(), None)
    elif attackerMove == "b":
        applyEffects(attacker, target, attackerMove, targetMove, *vampiricClaws(), None)
    elif attackerMove == "d":
        applyEffects(attacker, target, attackerMove, targetMove, *drainLife())
    elif attackerMove == "e":
        print(f"{attacker['name']} does nothing.")

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

print(f"\nLet the duel between {player1['name']} and {player2['name']} begin!")

night = 1
while(player1['health'] > 0 and player2['health'] > 0):
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

    player1Move = input(f"Player 1 ({player1['name']}), choose your move: ").lower()
    player2Move = input(f"Player 2 ({player2['name']}), choose your move: ").lower()

    print("\nMove Effects:")
    if not player1Move == 'c': print("----------")
    moveEffects(player1Move, player2Move, player1, player2)
    if not player1Move == 'c': print("----------")
    moveEffects(player2Move, player1Move, player2, player1)
    

    input("\n\nPress Enter to continue...")
    night += 1

#not done yet
#things to add:
#rest per 3 nights
#winner announcement
#update text prompts