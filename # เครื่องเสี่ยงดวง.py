# เครื่องเสี่ยงดวง
import random
import time
name = input("What's your name:")
Greeting = ['Hi!','Hello!','What up!','Nice to see you!']
grt = random.choice(Greeting)
time.sleep(1)
print(grt,name)
import random
filps = 0
roll = 0
HTcount = [0,0] #'Heads','Tails'
DNumb = [0,0,0,0,0,0] #Number of Dice 1,2,3,4,5,6

while True:
    print("F for FlipCoin, R for RollDice, S for Stop")
    ans = input("What kind of random [F|R|S]:") 
    if ans == 'F':
        Coin = random.randint(0,1)
        filps += 1
        if Coin == 0:
            time.sleep(1)
            print("Heads")
            HTcount[0] += 1
        if Coin == 1:
            time.sleep(1)
            print("Tails")
            HTcount[1] += 1
    if ans == 'R':
        Dice = random.randint(1,6)
        time.sleep(1)
        print(Dice)
        roll += 1
        if Dice == 1:
            DNumb[0] += 1
        elif Dice == 2:
            DNumb[1] += 1
        elif Dice == 3:
            DNumb[2] += 1
        elif Dice == 4:
            DNumb[3] += 1
        elif Dice == 5:
            DNumb[4] += 1
        elif Dice == 6:
            DNumb[5] += 1     
    if ans == 'S':
        time.sleep(1)
        print("Coins you fliped",filps)
        print("Dices you rolled",roll)
        print("Head/Tail count",HTcount)
        print("Number of Dices",DNumb)
        print("Good luck!")
        break