#!/usr/bin/python3

import lib_lottery as ll


def start_game():
    total_user_points = 0
    ll.clear()
    print("""Hi sweety! Let's gamble for a while.
           I'm about to draw 6 numbers from 1 to 49.
           Let's see how many of them you're going to guess.

           6 number match = 1 000 000 points
           5 number match = 100 000 points
           4 number match = 10 000 points
           3 number match = 1 000 points
           2 number match = 100 points
           1 number match = 10 points

           To exit press ctrl+C in GNU/Linux. 
           If you're using Windows you better switch to GNU/Linux now.
           For more info https://www.youtube.com/watch?v=xSkCny-HtTw
           """)
    while True:
        print(f'your current score is {total_user_points}')
        lucky_numbers = ll.draw_lots()
        user_numbers = ll.user_numbers()
        print('drawing lots')
        ll.animated_loading()
        print(f'lucky numbers today are {lucky_numbers}')
        print(f'you have chosen {user_numbers}')
        match = ll.comparer(lucky_numbers, user_numbers)

        user_points = 0
        if match == 6:
            user_points += 1000000
        elif match == 5:
            user_points += 100000
        elif match == 4:
            user_points += 10000
        elif match == 3:
            user_points += 1000
        elif match == 2:
            user_points += 100
        elif match == 1:
            user_points += 10
        else:
            user_points = 0

        total_user_points += user_points

        print(f"congrats! you've chosen {match} numbers right \nyour score is {user_points}")

    return 0


if __name__ == '__main__':
    start_game()
