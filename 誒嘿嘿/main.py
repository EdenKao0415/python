import random
import time

def displayIntro():
    print('''
You are in a land full of dragons. In front of you,
you see ten caves. In some cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
    print()


def totalCave():
    max=''
    while True:
        print('How  many cave do you want ? (minimum >= 10 )')
        max = input()
        if max.isdigit() and 0<int(max)>=10:
            break
    return max

def chooseCave(caveMax):
    cave = ''
    while True:
        print('Which cave will you go into? (1 to '+ caveMax+' )')
        cave = input()
        #print(cave)
        if cave.isdigit() and 0 < int(cave) <= int(caveMax) : #判斷是不是數字 cave.isdigit()
            break
    return cave

def checkCave(chosenCave,caveMax):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)


    badCave = int(0)
    while badCave%2 == 0:
        badCave = random.randint(3,int(caveMax)-1)
        #badCave = random.randint(3, 9)
    #print(badCave)
    badDragon = []  # 壞龍的陣列
    while len(badDragon)< badCave : # len()查看陣列裡面的數量 有沒有<friendlyCave
        num = random.randint(1,int(caveMax))
        if num not in badDragon : # num 亂數不再龍洞的陣列裡
            badDragon.append(num) #把亂數存到壞讀歐惡真列
    #print(badDragon)
    if int(chosenCave) not in badDragon:
         print('Gives you his treasure!')
    else:
         print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y' or playAgain == 'Y' or playAgain == 'YES' :
    displayIntro()
    caveMax= totalCave()
    caveNumber = chooseCave(caveMax)
    checkCave(caveNumber, caveMax)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
if playAgain != 'yes' or playAgain != 'y' or playAgain != 'Y' or playAgain != 'YES':
    print('我做的哈哈')
