#!/usr/bin/python3

from random import shuffle
from os import system, name
from sys import stdout
from time import sleep


def draw_lots():
    '''
    creates a list of ints from 1 to 49, shuffles it, slices first 6 elements
    :return: list of 6 random ints from 1 to 49
    '''
    lst = [i for i in range(1, 50)]
    shuffle(lst)
    short_lst = lst[0:6]
    short_lst.sort()
    return short_lst


def user_numbers():
    '''
    handles user input. User is supposed to introduce 6 ints from 1 to 49
    :return: list of 6 ints from 1 to 49
    '''
    lst = []
    while len(lst) < 6:
        str_num = input(f'{len(lst) + 1}. enter integer number from 1 to 49: \n')

        try:
            int_num = int(str_num)
        except ValueError:
            print("it's not an int number! Try again.\n")
            continue

        if int_num < 1 or int_num > 49:
            print('number is not in range from 1 to 49. please try again.')
            continue

        if int_num in lst:
            print("You've already introduced this number!")
            continue
        else:
            lst.append(int_num)

    lst.sort()
    return lst


def comparer(lucky_numbers, user_numbers):
    """
    compares two lists and returns how many items are the same.
    :param lucky_numbers: list of numbers chosen by draw lots. list of 6 ints from 1 to 49
    :param user_numbers: guesses of user. list of 6 numbers
    :return: how many numbers matches between two lists
    """
    match = 0
    for i in range(6):
        for ii in range(6):
            if user_numbers[i] == lucky_numbers[ii]:
                match += 1
    return match


def clear():
    """
    clears terminal
    :return: None
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def animated_loading():
    """
    animation of fake loading
    :return: none
    """
    chars = "/—\|"
    for i in range(5):
        for char in chars:
            stdout.write('\r' + char)
            sleep(.05)
            stdout.flush()
