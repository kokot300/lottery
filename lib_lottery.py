#!/usr/bin/python3

from random import shuffle
from os import system, name
from sys import stdout
from time import sleep


def draw_lots():
    lst = [i for i in range(1, 50)]
    shuffle(lst)
    short_lst = lst[0:6]
    short_lst.sort()
    return short_lst


def user_numbers():
    lst = []
    while len(lst) < 6:
        repetition_flag = False
        str_num = input('enter integer number from 1 to 49: \n')
        try:
            int_num = int(str_num)
            if int_num < 1 or int_num > 49:
                print('number is not in range from 1 to 49. please try again.')
                continue
            for i in range(len(lst)):
                if lst[i] == int_num:
                    repetition_flag = True
                    print("You've already introduced this number!")
                    break
            if repetition_flag == False:
                lst.append(int_num)
        except:
            print("it's not an int number! Try again.\n")
            continue
    lst.sort()
    return lst


def comparer(lucky_numbers, user_numbers):
    match = 0
    for i in range(6):
        for ii in range(6):
            if user_numbers[i] == lucky_numbers[ii]:
                match += 1
    return match


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def animated_loading():
    chars = "/—\|"
    for i in range(5):
        for char in chars:
            stdout.write('\r' + char)
            sleep(.05)
            stdout.flush()
