import random
import sys
from  art import  logo
print(logo)

print("welcome to guess the number")
number=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']
print("i am thinking number  from 1 to 100")
choice=['Easy','HARD']
num=random.choice(number)
num=int(num)
def easy():
    print("you have 10 guesses to start with")
    guess=10
    user_guess=None

    while num != user_guess:
        user_guess = int(input("guess number:"))
        print("wrong guess")
        if (user_guess > num):
            print("too high ")
        if user_guess < num:
            print("too low")
        guess-=1
        print(f"you have {guess} left ")
        if guess==0:
            print("your all guesses used you lose! :)")
            break
    if(user_guess==num):
        print(f"you win!!! the number was: {num}")


def hard():
    print("you have 5 guesses to start with")
    guess=5
    user_guess=None

    while num != user_guess:
        user_guess = int(input("guess number:"))
        print("wrong guess")
        if (user_guess > num):
            print("too high ")
        if user_guess < num:
            print("too low")
        guess-=1
        print(f"you have {guess} left ")
        if guess==0:
            print("your all guesses used you lose! :)")
            break
    if(user_guess==num):
        print(f"you win!!! the number was: {num}")

difficulty=str(input("Enter the difficulty level (EASY OR HARD) :").upper())
if difficulty=='EASY':
    easy()
elif difficulty=='HARD':
    hard()
else:
    print("wrong input")
    sys.exit()





