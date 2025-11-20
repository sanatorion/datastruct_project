import os

moves = { 
    #name: energy, damage, heal
    "daggerSlash": [6, 10,0],
    "vampiricClaws": [25, 40, 0],
    "dodge": [10, 0, 0],
    "drain":[13, 6, 10]
}

def printStatus(player):
    for key, value in player.items():
        symbol = '✚' if key == 'health' else '🗲'
        if key != 'pcount':
            if key == 'name':
                print(f"{key.capitalize()}: ({value})")
            else:
                print(f"{symbol} {key.capitalize()}: {value}")

def printBothStats(player1, player2):
    print("=======Player Status=======")
    printStatus(player1)
    print("---------------------------")
    printStatus(player2)
    print("---------------------------")
        
def applyEffects(attacker, target, attackerMove, targetMove, energyVal, damageVal, healVal):
    movePerLetter = {'A' : 'DAGGER SLASH', 'B' : 'VAMPIRIC CLAWS', 'C' : 'DODGE: BAT FORM', 'D' : 'DRAIN LIFE'}
    damageVal = 0 if targetMove == 'C' else damageVal

    print(f"Player {attacker['pcount']} ({attacker['name']}) uses {movePerLetter[attackerMove]}.")
    print(f"• Energy Used: {energyVal}")
    if attackerMove != 'C': print(f"• Damage Dealt: {damageVal}")
    attacker['energy'] = 0 if attacker['energy'] < energyVal else attacker['energy'] - energyVal
    target['health'] -= damageVal

    if target['health'] < 0:
        target['health'] = 0

    if attackerMove == 'D' and targetMove != 'C':
        print(f"• Health Gained: {healVal}")
        attacker['health'] += healVal

def moveEffects(attackerMove, targetMove, attacker, target):
    match attackerMove:
        case 'A': #dagger slash
            applyEffects(attacker, target, attackerMove, targetMove, *moves['daggerSlash']) 
        case 'B': #vampiric claws
            applyEffects(attacker, target, attackerMove, targetMove, *moves['vampiricClaws'])
        case 'C': #dodge
            applyEffects(attacker, target, attackerMove, targetMove, *moves['dodge'])
        case 'D': #drain life
            applyEffects(attacker, target, attackerMove, targetMove, *moves['drain'])
        case 'E': #do nothing
            print(f"Player {attacker['pcount']} ({attacker['name']}) does nothing.")

def rest(player):
    heal = 20 if player['energy'] == 0 else 25
    energy = 13 if player['energy'] == 0 else 20
    if player['energy'] == 0:
        print(f"Player {player['pcount']} ({player['name']}) is too tired, and can only rest partially...")
    else:
        print(f"Player {player['pcount']} ({player['name']}) is able to have a complete rest.")
    print(f"Player {player['pcount']} ({player['name']}) heals for {heal} and replenishes {energy} energy.")
    player['health'] += heal
    player['energy'] += energy

    if player['energy'] > 50:
        player['energy'] = 50
    
def getValidInput(player):
    choices = ['A', 'B', 'C', 'D', 'E']
    if player['energy'] != 0:
        while(True):
            playerInput = input(f"Player {player['pcount']} ({player['name']}): ")
            if playerInput in choices: 
                return playerInput
            print("Only A, B, C, D, or E is allowed.\n")
    else:
        input(f"Player {player['pcount']} ({player['name']}) has no more energy. Skipping this turn...")
        return 'E'

#main
print("Welcome Vampire Spawn!\n")
print("Fight for the right to ascend into a Vampire lord")
print("Attempt to knockout your opponent.")
print("Use your vampiric moves to outsmart your opponent.")
print("\nPlayers enter your names...")

player1Name = input("Player 1: ")
player2Name = input("Player 2: ")
print()
playAgain = "Y"
while playAgain == 'Y':
    print(f"Let the duel between {player1Name} and {player2Name} begin!\n")
    player1 = {
        "name": player1Name,
        "health": 100,
        "energy": 50,
        "pcount": 1
    }
    player2 = {
        "name": player2Name,
        "health": 100,
        "energy": 50,
        "pcount": 2
    }
    input("Press any key to continue...")

    os.system('cls')
    night = 1
    round = 0
    while player1['health'] > 0 and player2['health'] > 0:
        if round == 3:
            os.system('cls')
            night += 1
            round = 0
            print("The night has passed. Both vampire spawns shall rest...\n")
            rest(player1)
            print("----------")
            rest(player2)
        
            input("\nPress any key to continue...")
            print()

        round += 1
        os.system('cls')
        print(f"~ ☆ • ° . Night {night} . ° • ☆ ~")
        print(f"⎯⎯⎯⎯⎯⎯⎯⎯⎯ Round {round} ⎯⎯⎯⎯⎯⎯⎯⎯⎯")
        printBothStats(player1, player2)

        print("\n======Available Moves======")
        print(f"A. DAGGER SLASH ({moves['daggerSlash'][1]} damage; energy: {moves['daggerSlash'][0]})")
        print(f"B. VAMPIRIC CLAWS ({moves['vampiricClaws'][1]} damage; energy: {moves['vampiricClaws'][0]})")
        print(f"C. DODGE: BAT FORM (nullifies incoming attack; energy: {moves['dodge'][0]})")
        print(f"D. DRAIN LIFE (deals {moves['drain'][1]} damage then heals self by {moves['drain'][2]}; energy: {moves['drain'][0]})")
        print("E. Do nothing (energy: 0)\n")

        print("Players, what are your moves? \nPlease enter A, B, C, D, or, E only")
        player1Move = getValidInput(player1)
        player2Move = getValidInput(player2)

        os.system('cls')
        print("=======Moves Effects=======")
        moveEffects(player1Move, player2Move, player1, player2)
        print("----------")
        moveEffects(player2Move, player1Move, player2, player1)

        input("\nPress any key to continue...")
        print()
    
    os.system('cls')
    printBothStats(player1, player2)

    if player1['health'] == player2 ['health']:
        print(f"Draw! As both {player1['name']} and {player2['name']} fail to ascend...")
    elif player1['health'] > player2['health']:
        print(f"Player 1 ({player1['name']}) wins! Player 1 ascends to a Vampire Lord...")
    else:
        print(f"Player 2 ({player2['name']}) wins! Player 2 ascends to a Vampire Lord...")

    print("\nWould you like to Play Again?")
    playAgain = input("Type (Y) to Play Again: ")
    os.system('cls')