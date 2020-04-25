import time
from multiprocessing import Process
from random import randint

from doom_guess_number_game.loader import print_logo, play_music

p1 = Process(target=play_music)
p1.start()
while True:
    print_logo()
    number = randint(1, 10)
    while True:
        user_number = input('Please define number from 1 to 10 - ')
        if user_number.isdigit() and 1 <= int(user_number) <= 10:
            break
        elif user_number.isdigit() and int(user_number) == 666:
            print('HEHEH, AVE 𖤐, but try again')
            continue
        print('Are you dumb?! 1 to 10...Try again, genius...')
    if int(user_number) == number:
        print('\nGG Sherlock! it\'s correct')
    else:
        print(f'\nGG IZI. My number was - {number}')
    next_game = None
    while True:
        wanna_more = input('\nWanna more (y/n)? ')
        if wanna_more.strip().lower() == 'y':
            print('\nWise choice!')
            time.sleep(0.5)
            next_game = True
            break
        elif wanna_more.strip().lower() == 'n':
            print('\nWalk on home boy!')
            next_game = False
            break
        else:
            print('Oh dear...Y or N, suka!')
    if not next_game:
        break
p1.terminate()
