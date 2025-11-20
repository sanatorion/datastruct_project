#group version

import animation, os
moves = { 
    #name: energy, damage, heal
    "daggerSlash": [6, 10,0],
    "vampiricClaws": [25, 40, 0],
    "dodge": [10, 0, 0],
    "drain":[13, 6, 10]
}

effectsPerPlayer = {
    1: {'health': 0, 'energy': 0},
    2: {'health': 0, 'energy': 0}
}

delay = 0.05
delayPerStatResult = 0.5
def printBothStats(player1, player2, perLine):
    if perLine:
        animation.printPerLine( 0,
            "=======Player Status=======",
            *printStatus(player1),
            "---------------------------",
            *printStatus(player2),
            "---------------------------", )
    else:
        print("=======Player Status=======")
        for message in printStatus(player1):
            print(message)
        print("---------------------------")
        for message in printStatus(player2):
            print(message)
        print("---------------------------")
            
def updateStats(player1, player2):
    while any(value for _, stats in effectsPerPlayer.items() for _, value in stats.items()):
        animation.restorepos()
        printBothStats(player1, player2, False)

        #increment or decrement stats by 1
        for player, stats in effectsPerPlayer.items():
            player = player1 if player == 1 else player2
            for key, _ in stats.items():
                if stats[key] < 0:
                    stats[key] += 1
                    player[key] -= 1
                    if key == 'energy' and player[key] == 0:
                        stats[key] = 0

                elif stats[key] > 0:
                    stats[key] -= 1
                    player[key] += 1
        
        animation.time.sleep(0.10)
    animation.restorepos()
    printBothStats(player1, player2, False)
        

def reseteffectsPerPlayer():
    for key in range (1, 3):
        effectsPerPlayer[key]['health'] = 0
        effectsPerPlayer[key]['energy'] = 0

def printStatus(player):
    messages = []
    for key, value in player.items():
        symbol = '✚' if key == 'health' else '🗲'

        if key != 'pcount':
            if key == 'name':
                messages.append(f"{key.capitalize()}: ({value})")
            else:
                positiveORnegative = f"{'+' if effectsPerPlayer[player['pcount']][key] > 0 else ''}"
                statEffect = f"({positiveORnegative}{effectsPerPlayer[player['pcount']][key]})" if effectsPerPlayer[player['pcount']][key] != 0 else ''
                messages.append(f"{symbol} {key.capitalize()}: {value} {statEffect}     ")
    return messages

def applyEffects(attacker, target, attackerMove, targetMove, energyVal, damageVal, healVal, applydelays):
    movePerLetter = {'A' : 'DAGGER SLASH', 'B' : 'VAMPIRIC CLAWS', 'C' : 'DODGE', 'D' : 'DRAIN LIFE'}
    damageVal = 0 if targetMove == 'C' else damageVal

    animation.printPerChar(f"Player {attacker['pcount']} ({attacker['name']}) uses {movePerLetter[attackerMove]}.", False, 0, False, True)
    if applydelays: animation.time.sleep(delayPerStatResult)
    print(f"• Energy Used: {energyVal}")
    if applydelays: animation.time.sleep(delayPerStatResult)
    if attackerMove != 'C': print(f"• Damage Dealt: {damageVal}")

    effectsPerPlayer[attacker['pcount']]['energy'] -= energyVal
    effectsPerPlayer[target['pcount']]['health'] -= damageVal


    if attackerMove == 'D' and targetMove != 'C':
        if applydelays: animation.time.sleep(delayPerStatResult)
        print(f"• Health Gained: {healVal}")
        effectsPerPlayer[attacker['pcount']]['health'] += healVal

def moveEffects(attackerMove, targetMove, attacker, target, applydelays):
    match attackerMove:
        case 'A': #dagger slash
            applyEffects(attacker, target, attackerMove, targetMove, *moves['daggerSlash'], applydelays)
        case 'B': #vampiric claws
            applyEffects(attacker, target, attackerMove, targetMove, *moves['vampiricClaws'], applydelays)
        case 'C': #dodge
            applyEffects(attacker, target, attackerMove, targetMove, *moves['dodge'], applydelays)
        case 'D': #drain life
            applyEffects(attacker, target, attackerMove, targetMove, *moves['drain'], applydelays)
        case 'E': #do nothing
            animation.printPerChar(f"Player {attacker['pcount']} ({attacker['name']}) does NOTHING.", False, 0, False, True)

def rest(player):
    heal = 20 if player['energy'] == 0 else 25
    energy = 13 if player['energy'] == 0 else 20
    if player['energy'] == 0:
        animation.printPerChar(f"Player {player['pcount']} ({player['name']}) is too tired, and can only rest partially...", False, 1, True, True)
    else:
        animation.printPerChar(f"Player {player['pcount']} ({player['name']}) is able to have a complete rest.", False, 1, True, True)
    animation.printPerLine( delayPerStatResult,
        f"• Health Gained: {heal}",
        f"• Energy Replenished: {energy}",
        )
    effectsPerPlayer[player['pcount']]['health'] += heal
    effectsPerPlayer[player['pcount']]['energy'] += energy

def getValidInput(player):
    choices = ['A', 'B', 'C', 'D', 'E']
    if player['energy'] != 0:
        while(True):
            animation.clearLine(False)
            animation.printPerChar(f"\rPlayer {player['pcount']} ({player['name']}): ", False, delay, False, False)
            playerInput = input()
            if playerInput in choices: 
                return playerInput
            animation.clearLine(True)
            animation.printPerChar("Only A, B, C, D, or E is allowed.", False, 1, False, False)

            
    else:
        animation.printPerChar(f"Player {player['pcount']} ({player['name']}) has no more energy. Skipping this turn...", False, 1, False, False)
        return 'E'
    
#==========MAIN=============
playAgain = "Y"
while playAgain == 'Y':
    os.system('cls')
    print("======================")
    print("  VAMPIRE DUEL ARENA")
    print("======================")
    animation.time.sleep(1)

    animation.printPerChar("Welcome Vampire Spawn!\n", False, 1, True, True)
    animation.printPerChar("Fight for the right to ascend into a Vampire lord.", False, 0, True, True)
    animation.printPerChar("Attempt to knockout your opponent.", False, 0, True, True)
    animation.printPerChar("Use your vampiric moves to outsmart your opponent.", False, 0, True, True)
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
    night = 1
    round = 0
    while player1['health'] > 0 and player2['health'] > 0:
        os.system('cls')
        if round == 3:
            round = 0
            night += 1
            animation.printPerChar("The night ends. Both vampire spawns shall rest...", False, 1, True, True)
            print()
            animation.savepos()
            printBothStats(player1, player2, True)

            print()
            rest(player1)
            print("---------------------------")
            animation.time.sleep(1.5)
            updateStats(player1, player2)
            reseteffectsPerPlayer()
            
            animation.time.sleep(1)
            print("\n\n\n\n")
            rest(player2)
            animation.time.sleep(1.5)
            updateStats(player1, player2)
            reseteffectsPerPlayer()
        
            animation.time.sleep(1.5)
            os.system('cls')

        round += 1
        animation.printPerChar(f"~ ☆ • ° . Night {night} . ° • ☆ ~", False, 0, False, True)
        animation.printPerChar(f"⎯⎯⎯⎯⎯⎯⎯⎯⎯ Round {round} ⎯⎯⎯⎯⎯⎯⎯⎯⎯", False, 1, False, True)
        printBothStats(player1, player2, True)
        
        animation.printPerLine( 0,
            "\n======Available Moves======",
            f"A. DAGGER SLASH ({moves['daggerSlash'][1]} damage; energy: {moves['daggerSlash'][0]})",
            f"B. VAMPIRIC CLAWS ({moves['vampiricClaws'][1]} damage; energy: {moves['vampiricClaws'][0]})",
            f"C. DODGE: BAT FORM (nullifies incoming attack; energy: {moves['dodge'][0]})",
            f"D. DRAIN LIFE (deals {moves['drain'][1]} damage then heals self by {moves['drain'][2]}; energy: {moves['drain'][0]})",
            "E. Do NOTHING (energy: 0)\n"
        )

        print("Choose your moves")
        player1Move = getValidInput(player1)
        animation.clearLine(True)
        player2Move = getValidInput(player2)

        os.system('cls')
        print(f"~ ☆ • ° . Night {night} . ° • ☆ ~")
        print(f"⎯⎯⎯⎯⎯⎯⎯⎯⎯ Round {round} ⎯⎯⎯⎯⎯⎯⎯⎯⎯")
        animation.savepos()
        printBothStats(player1, player2, False)
        animation.printPerChar("\n=======Moves Effects=======", False, 1, False, True)

        moveEffects(player1Move, player2Move, player1, player2, True) #player1
        animation.time.sleep(delayPerStatResult)
        print("---------------------------")
        animation.time.sleep(1.5)
        if player1Move != 'E': 
            updateStats(player1, player2)
            reseteffectsPerPlayer()

            animation.time.sleep(1)
            if player1Move == 'C':
                print("\n\n\n\n")   
            elif player1Move == 'D':
                if player2Move == 'C':
                    print("\n\n\n\n\n")
                else:
                    print("\n\n\n\n\n\n")
            else:
                print("\n\n\n\n\n")

        moveEffects(player2Move, player1Move, player2, player1, True) #player2
        animation.time.sleep(1.5)
        if player2Move != 'E':
            updateStats(player1, player2)
            reseteffectsPerPlayer()
        animation.time.sleep(1.5)
    
    os.system('cls')
    print(f"~ ☆ • ° . Night {night} . ° • ☆ ~")
    print(f"⎯⎯⎯⎯⎯⎯⎯⎯⎯ Round {round} ⎯⎯⎯⎯⎯⎯⎯⎯⎯")
    printBothStats(player1, player2, False)
    print()
    if player1['health'] == player2 ['health']:
        animation.printPerChar(f"Draw! As both {player1['name']} and {player2['name']} fail to ascend...", False, 1.5, False, True)
    elif player1['health'] > player2['health']:
        animation.printPerChar(f"Player 1 ({player1['name']}) wins! Player 1 ascends to a Vampire Lord...", False, 1.5, False, True)
    else:
        animation.printPerChar(f"Player 2 ({player2['name']}) wins! Player 2 ascends to a Vampire Lord...", False, 1.5, False, True)
    animation.printPerChar("\nWould you like to Play Again?", False, 0, False, True)
    playAgain = input("Type (Y) to Play Again: ")