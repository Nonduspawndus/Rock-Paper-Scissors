import random
import time
print("Welcome to Rock, Paper, Scissors \nRules: \nYou will get 5 chances in one session. \nIf you get 3 or more points, you win. \nRepresentations: \nRock: r, Paper: p, Scissors: s")
rps = ['r', 'p', 's']
while True:
    score = 0
    count = 0
    for chance in range(5):
        choice = input("Enter your choice: ")
        comp = random.choice(rps)
        while choice not in rps:
            print("Invalid Choice. Please enter again.")
            count += 1
            if count == 10:
                break
            else:
                continue
        if (choice == 'r' and comp == 's') or (choice == 'p' and comp == 'r') or (choice == 's' and comp == 'p'):
            score += 1
            print(choice, "V/S", comp)
            print("You earned a point! :)")
        elif choice == comp:
            print(choice, "V/S", comp)
            print("You tied! :|")
        else:
            print(choice, "V/S", comp)
            print("You lost a point! :(")
    if score>= 3:
        string = ". You Won! :)"
    if score< 3:
        string = ". You Lost! :("
    print("Total points:", score, string)
    time.sleep(2)
    print("If you want to play again: type 'play' \nIf you want to quit: type 'exit'")
    answer = input('>')
    if answer == 'play':
        continue
    if answer == 'exit':
        break
