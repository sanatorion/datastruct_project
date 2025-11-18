#group version
import animation, os, cursor

moves = { 
    #name: energy, damage, heal
    "daggerSlash": [6, 10,0],
    "vampiricClaws": [25, 40, 0],
    "dodge": [10, 0, 0],
    "drain":[13, 6, 10]
}

delay = 0.05
def printBothStats(player1, player2):
    animation.printPerLine(
        "=======Player Status=======",
        *printStatus(player1),
        "---------------------------",
        *printStatus(player2),
        "---------------------------",
    )

def printStatus(player):
    messages = []
    
    for key, value in player.items():
        symbol = '✚' if key is 'health' else '🗲'

        if key != 'pcount':
            if key == 'name':
                messages.append(f"{key.capitalize()}: ({value})")
            else:
                messages.append(f"{symbol} {key.capitalize()}: {value}")
    return messages

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
            applyEffects(attacker, target, attackerMove, targetMove, *moves['daggerSlash']) 
        case 'B': #vampiric claws
            applyEffects(attacker, target, attackerMove, targetMove, *moves['vampiricClaws'])
        case 'C': #dodge
            applyEffects(attacker, target, attackerMove, targetMove, *moves['dodge'])
        case 'D': #drain life
            applyEffects(attacker, target, attackerMove, targetMove, *moves['drain'])
        case 'E': #do nothing
            print(f"Player {attacker['pcount']} ({attacker['name']}) does NOTHING.")

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

def getValidInput(player):
    choices = ['A', 'B', 'C', 'D', 'E']
    if player['energy'] != 0:
        while(True):
            animation.printPerChar(f"\rPlayer {player['pcount']} ({player['name']}): ", False, delay, False, False)
            playerInput = input()
            if playerInput in choices: 
                return playerInput
            print("Only A, B, C, D, or E is allowed.\n")
            
    else:
        input(f"Player {player['pcount']} ({player['name']}) has no more energy. Skipping this turn...")
        return 'E'

#main
playAgain = "Y"
while playAgain == 'Y':
    os.system('cls')
    print("======================")
    print("  VAMPIRE DUEL ARENA")
    print("======================")
    animation.time.sleep(1)

    animation.printPerChar("Welcome Vampire Spawn!\n", False, 1, True, True)
    animation.printPerChar("Fight for the right to ascend into a Vampire lord.", True, 0, True, False)
    animation.printPerChar("Attempt to knockout your opponent.", True, 0, True, False)
    animation.printPerChar("Use your vampiric moves to outsmart your opponent.", True, 0, True, False)
    print()
    animation.printPerChar("Players enter your names...", False, 0, False, True)
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
    print()
    animation.printPerChar(f"Let the duel between {player1['name']} and {player2['name']} begin!", False, 1, False, True)
    os.system('cls')
    night = 0
    while player1['health'] > 0 and player2['health'] > 0:
        os.system('cls')
        if night > 0 and night % 3 == 0:
            printBothStats(player1, player2)
            print()
            print("3 nights have passed. Both vampire spawns shall rest...")
            rest(player1)
            print("----------")
            rest(player2)
        
            input("\nPress any key to continue...")
            print()
        night += 1

        animation.printPerChar(f"~ ☆ • ° . Night {night} . ° • ☆ ~", False, 1, False, True)
        printBothStats(player1, player2)
        
        animation.printPerLine(
            "\n======Available Moves======",
            f"A. DAGGER SLASH ({moves['daggerSlash'][1]} damage; energy: {moves['daggerSlash'][0]})",
            f"B. VAMPIRIC CLAWS ({moves['vampiricClaws'][1]} damage; energy: {moves['vampiricClaws'][0]})",
            f"C. DODGE: BAT FORM (nullifies incoming attack; energy: {moves['dodge'][0]})",
            f"D. DRAIN LIFE (deals {moves['drain'][1]} damage then heals self by {moves['drain'][2]}; energy: {moves['drain'][0]})",
            "E. Do NOTHING (energy: 0)\n"
        )

        print("Choose your moves")
        player1Move = getValidInput(player1)
        print('\033[F\033[2K', end = '')
        player2Move = getValidInput(player2)

        print("\nMove Effects:")
        moveEffects(player1Move, player2Move, player1, player2)
        print("----------")
        moveEffects(player2Move, player1Move, player2, player1)

        input("\nPress any key to continue...")
        print()

    printBothStats(player1, player2)

    if player1['health'] == player2 ['health']:
        print(f"Draw!")
    elif player1['health'] > player2['health']:
        print(f"Player 1 ({player1['name']}) wins! Player 1 ascends to a Vampire Lord...")
    else:
        print(f"Player 2 ({player2['name']}) wins! Player 2 ascends to a Vampire Lord...")

    print("\nWould you like to Play Again?")
    playAgain = input("Type (Y) to Play Again: ")
    print()