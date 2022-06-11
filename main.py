"""

SkipFly Coded by Fijo.
A simple python script used to bypass ANY AdFly link.


"""



import os
import time
import crayons
import sys
import random

from bs4 import BeautifulSoup
import colorama
from colorama import init
from colorama import Fore, Style
from pystyle import Colorate, Colors, Write, Box

from tkinter import *



def clear():
        os.system('cls')

clear()


def logo():
    try:
        text = """                                   

                        ███████╗██╗  ██╗██╗██████╗ ███████╗██╗  ██╗   ██╗
                        ██╔════╝██║ ██╔╝██║██╔══██╗██╔════╝██║  ╚██╗ ██╔╝
                        ███████╗█████╔╝ ██║██████╔╝█████╗  ██║   ╚████╔╝ 
                        ╚════██║██╔═██╗ ██║██╔═══╝ ██╔══╝  ██║    ╚██╔╝  
                        ███████║██║  ██╗██║██║     ██║     ███████╗██║   
                        ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝   
                                                 
                                                                             
                                                                             \n                    
        """
        bad_colors = ['RED', 'WHITE']
        codes = vars(colorama.Fore)
        colors = [codes[color] for color in codes if color in bad_colors]
        colored_chars = [random.choice(colors) + char for char in text]
        print(''.join(colored_chars))
        print(Fore.RESET + "\t\t\t               Coded by: xFijo#0999\n")

    except KeyboardInterrupt:
        sys.exit()

clear()
logo()

q1 = input(Colorate.Horizontal(Colors.red_to_white, f'Do you want to launch SkipFly ? [Y/N] : '))
if q1 == 'N' or q1 == 'n':
    print(Colorate.Horizontal(Colors.red_to_white, f'Closing SkipFly.....'))
if q1 == 'Y' or q1 == 'y':
    print(Colorate.Horizontal(Colors.red_to_white, f'Welcome to SkipFly!'))
    link = input(Colorate.Horizontal(Colors.red_to_white, f'AdFly Link : '))
    link = link.split('&dest=')[1]
else:
    print(Colorate.Horizontal(Colors.red_to_white, f'Please input a valid argument. (Y or N)'))
    
giveLink = input(Colorate.Horizontal(Colors.red_to_white, f'Type Y to get link.'))
if giveLink == 'Y' or giveLink == 'y':
    print(crayons.green(link))
    print(crayons.green('Link generated! remove all of the "3A", "2F" and the "%" then paste it into your browser!'))
else: 
    print(crayons.red('Link not provided!'))
pass

print('\n')
print('\n')
print('\n')
print(Colorate.Horizontal(Colors.red_to_white, f'Thank you for using SkipFly. Your support is always appreciated!'))
