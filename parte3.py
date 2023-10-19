# Jogo - Adivinhe onde está o objeto
from random import shuffle
example = [1,2,3,4,5,6,7,8,9]
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result = shuffle_list(example)
print(result)

mylist = [' ', 'o',' ']
shuffle_list(mylist)
def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("pick a number: 0, 1, 2")
    return int(guess)
player_guess()
myindex = player_guess
print(myindex)
def check_guess(mylist, guess):
    if mylist[guess] == 'o':
        print("Correct!")
    else:
        print("Wrong guess")
        print(mylist)

mylist = [' ', 'o', ' ']
mixedup_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mixedup_list, guess)