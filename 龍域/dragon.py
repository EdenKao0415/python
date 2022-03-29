import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see ten caves. In some cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
    print()

def chooseCave():
    cave = ''
    while True:
        print('Which cave will you go into? (1 to 10 )')
        cave = input()
        print(cave)
        if cave.isdigit() and 1 < int(cave) <= 10 : #判斷是不是數字 cave.isdigit()
            break
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    badCave = int()
    if badCave> 3 and badCave%2 == 0:
        badCave = random.randint(3,9)
    #print(badCave)
    badDragon = [] #壞龍的陣列
    while len(badDragon)< badCave : # len()查看陣列裡面的數量 有沒有<friendlyCave
        num = random.randint(1,10)
        if num not in badDragon : # num 亂數不再龍洞的陣列裡
            badDragon.append(num) #把亂數存到壞讀歐惡真列
    #print(badDragon)
    if chosenCave != str(badDragon):
         print('Gives you his treasure!')
    else:
         print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y' or playAgain == 'Y' or playAgain == 'YES' :
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
if playAgain != 'yes' or playAgain != 'y' or playAgain != 'Y' or playAgain != 'YES':
    print('我做的哈哈')
