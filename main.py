moves = { 
    #name: energy, damage, heal
    "daggerSlash": [6, 10],
    "vampiricClaws": [25, 40],
    "dodge": 10,
    "drain":[13, 6, 10]
}

def printStatus(player):
    for key, value in player.items():
        if key != 'pcount':
            if key == 'name':
                print(f"{key.capitalize()}: ({value})")
            else:
                print(f"{key.capitalize()}: {value}")
        
def applyEffects(attacker, target, attackerMove, targetMove, energyVal, damageVal, healVal):
    damageVal = 0 if targetMove == 'C' else damageVal

    print(f"Player {attacker['pcount']} ({attacker['name']}) uses {energyVal} energy.")
    print(f"Player {target['pcount']} ({target['name']}) received {damageVal} damage.")

    attacker['energy'] = 0 if attacker['energy'] < energyVal else attacker['energy'] - energyVal
    target['health'] -= damageVal

    if attackerMove == 'D' and targetMove != 'C':
        print(f"Player {attacker['pcount']} ({attacker['name']}) gains {healVal} health.")
        attacker['health'] += healVal

def moveEffects(attackerMove, targetMove, attacker, target):
    match attackerMove:
        case 'A': #dagger slash
            applyEffects(attacker, target, attackerMove, targetMove, *moves['daggerSlash'], 0) 
        case 'B': #vampiric claws
            applyEffects(attacker, target, attackerMove, targetMove, *moves['vampiricClaws'], 0)
        case 'C': #dodge
            applyEffects(attacker, target, attackerMove, targetMove, moves['dodge'], 0, 0)
        case 'D': #drain life
            applyEffects(attacker, target, attackerMove, targetMove, *moves['drain'])
        case 'E': #do nothing
            print(f"Player {attacker['pcount']} ({attacker['name']}) chooses to do nothing.")

def rest(player):
    if player['energy'] == 0:
        print(f"Player {player['pcount']} ({player['name']}) is too tired, and can only rest partially...")
    else:
        print(f"Player {player['pcount']} ({player['name']}) is able to have a complete rest.")
    print(f"Player {player['pcount']} ({player['name']}) heals for {20 if player['energy'] == 0 else 25} and replenishes {13 if player['energy'] == 0 else 20} energy.")

    player['health'] += 20 if player['energy'] == 0 else 25
    player['energy'] += 13 if player['energy'] == 0 else 20

def getValidInput(player):
    choices = ['A', 'B', 'C', 'D', 'E']
    loop = True
    if player['energy'] != 0:
        while(loop):
            loop = False
            playerInput = input(f"Player {player['pcount']} ({player['name']}): ")

            if playerInput not in choices:
                print("Only A, B, C, D, or E is allowed.\n")
                loop = True
        return playerInput
    else:
        input(f"Player {player['pcount']} ({player['name']}) has no more energy. Skipping this turn...")

#main
playAgain = "Y"
while playAgain == 'Y':
    print("Welcome Vampire Spawn!\n")
    print("Fight for the right to ascend into a Vampire lord")
    print("Attempt to knockout your opponent.")
    print("Use your vampiric moves to outsmart your opponent.")
    print("\nPlayers enter your names...")
    player1 = {
        "name": input("Player 1: "),
        "health": 100,
        "energy": 50,
        "pcount": 1
    }
    player2 = {
        "name": input("Player 2: "),
        "health": 100,
        "energy": 50,
        "pcount": 2
    }
    print(f"\nLet the duel between {player1['name']} and {player2['name']} begin!\n")

    night = 0
    while player1['health'] > 0 and player2['health'] > 0:
        if night > 0 and night % 3 == 0:
            print("3 nights have passed. Both vampire spawns shall rest...")
            rest(player1)
            print("----------")
            rest(player2)
        
            input("\nPress any key to continue...")
            print()
        night += 1
        print(f"=== Night {night} ===\n==========")
        print("Player Status\n----------")
        printStatus(player1); print("----------")
        printStatus(player2); print("==========")

        print("\nAvailable Moves:" \
        f"\nA. Dagger Slash ({moves['daggerSlash'][1]} damage; energy: {moves['daggerSlash'][0]})" \
        f"\nB. Vampiric Claws ({moves['vampiricClaws'][1]} damage; energy: {moves['vampiricClaws'][0]})" \
        f"\nC. Dodge: Bat Form (nullifies incoming attack; energy: {moves['dodge']})" \
        f"\nD. Drain Life (deals {moves['drain'][1]} damage then heals self by {moves['drain'][2]}; energy: {moves['drain'][0]})" \
        "\nE. Do nothing (energy: 0)\n")

        print("Players, what are your moves? \nPlease enter A, B, C, D, or, E only")
        player1Move = getValidInput(player1)
        player2Move = getValidInput(player2)

        if player1Move != None and player2Move != None:
            print("\nMove Effects:")
            moveEffects(player1Move, player2Move, player1, player2)
            if player1Move != None or player2Move != None: print("----------")
            moveEffects(player2Move, player1Move, player2, player1)

        input("\nPress any key to continue...")
        print()

    print("==========")
    print("Player Status\n----------")
    printStatus(player1); print("----------")
    printStatus(player2); print("==========")

    if player1['health'] == player2 ['health']:
        print(f"Draw!")
    
    if player1['health'] > player2['health']:
        print(f"Player 1 ({player1['name']}) wins! Player 1 ascends to a Vampire Lord...")
    else:
        print(f"Player 2 ({player2['name']}) wins! Player 2 ascends to a Vampire Lord...")

    print("\nWould you like to Play Again?")
    playAgain = input("Type (Y) to Play Again: ")
    print()