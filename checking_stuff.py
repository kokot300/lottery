# import sys, time, threading
from sys import stdout
from time import sleep

# def the_process_function():
#     n = 20
#     for i in range(n):
#         time.sleep(1)
#         sys.stdout.write('\r'+'loading...  process '+str(i)+'/'+str(n)+' '+ '{:.2f}'.format(i/n*100)+'%')
#         sys.stdout.flush()
#     sys.stdout.write('\r'+'loading... finished               \n')

def animated_loading():
    chars = "/—\|"
    for i in range(5):
        for char in chars:
            stdout.write('\r'+char)
            sleep(.05)
            stdout.flush()

# the_process_function()
animated_loading()