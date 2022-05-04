from random import randint
import string, time
from tqdm import tqdm


# az_Upper = string.ascii_uppercase
# list1 = []
# random_str = ''
# for i in az_Upper:
#     list1.append(i)
# question_for_string_range = int(input("how much length of string you want? "))
# for i in range(0, question_for_string_range):
#     ran = randint(0, 2)
#     if ran == 0:
#         random_str += str(randint(0,9))
#     elif ran == 1:
#         random_str += list1[randint(0,25)]
#     else:
#         random_str += list1[randint(0,25)].lower()
# print("your id is ", random_str)
while True:
    for_skip = input("Do You Want To Skip Spins? (y/n) ").lower()
    skip = False
    if for_skip == "y":
        skip = True
        break
    elif for_skip != "y" and for_skip != "n":
        print("Invalid Input")
    else:
        break

def bonusspin(spins):
    my_coin = 0
    spin = spins
    gifts = [10,25,1500,100,2000,5,1,1500]
    print("you have ", spin, "spins")
    time.sleep(3)
    while spin >  0:
        number = randint(0, 9)
        if number == 0 or number == 1 or number == 2 or number == 3 or number == 4:
            num = randint(0, 4)
            if num == 0:
                my_coin += gifts[0]
                print(" 10 COIN!!")
                spin -= 1
                if not skip:
                    time.sleep(2)
            elif num == 1:
                my_coin += gifts[5]
                print(" 5 COIN!!")
                spin -= 1
                if not skip:
                    time.sleep(2)
            else:
                my_coin += gifts[6]
                print(" 1 coin")
                spin -= 1
                if not skip:
                    time.sleep(2)
        elif number == 5 or number == 6 or number == 7 or number == 8:
            num = randint(0, 3)
            if num == 0:
                my_coin += gifts[1]
                print(" 25 COIN!!")
                spin -= 1
                if not skip:
                    time.sleep(2)
            else:
                my_coin += gifts[3]
                print(" 100 COIN!!")
                spin -= 1
                if not skip:
                    time.sleep(2)
        else:
            num = randint(0, 1)
            if num == 0:
                my_coin += gifts[4]
                print(" 2000 COIN!!")
                spin -= 1
                if not skip:
                    time.sleep(2)
            elif num == 1:
                print("You Won 1 Free Spin")
                if not skip:
                    time.sleep(2)
            else:
                my_coin += gifts[7]
                print(" 1500 COIN!!")
                spin -= 1
                if not skip:
                    time.sleep(2)
def spinning():
    my_coin = 0
    spin = 5
    gifts = [10,25,1500,100,2000,5,1,1500]
    print("you have ", spin, "spins")
    time.sleep(3)
    while spin >  0:
        number = randint(0, 9)
        if number == 0 or number == 1 or number == 2 or number == 3 or number == 4:
            num = randint(0, 4)
            if num == 0:
                my_coin += gifts[0]
                print(" 10 COIN!!")
                spin -= 1
                if not skip:
                    time.sleep(2)
            elif num == 1:
                my_coin += gifts[5]
                print(" 5 COIN!!")
                spin -= 1
                if not skip:
                    time.sleep(2)
            else:
                my_coin += gifts[6]
                print(" 1 COIN!!")
                spin -= 1
                if not skip:
                    time.sleep(2)
        elif number == 5 or number == 6 or number == 7 or number == 8:
            num = randint(0, 3)
            if num == 0:
                my_coin += gifts[1]
                print(" 25 COIN!!")
                spin -= 1
                if not skip:
                    time.sleep(2)
            else:
                my_coin += gifts[3]
                print(" 100 COIN!!")
                spin -= 1
                if not skip:
                    time.sleep(2)
        else:
            num = randint(0, 1)
            if num == 0:
                my_coin += gifts[4]
                print(" 2000 COIN!!")
                spin -= 1
                if not skip:
                    time.sleep(2)
            elif num == 1:
                print("You Won 1 Free Spin")
                if not skip:
                    time.sleep(2)
            else:
                my_coin += gifts[7]
                print(" 1500 COIN!!")
                spin -= 1
                if not skip:
                    time.sleep(2)
    if my_coin > 3500:
        print("You Won 3500+ Coin And We Will Gave You Additional 3 spins, Good Luck <3 ")
        time.sleep(2)
        bonusspin(3)
    print("You Won ", my_coin, " coin")

        

spinning()












