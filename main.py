""" 
Created By SORENSHAMLOU

Create At : 2024/10/17

Update At : 2024/10/17

File Name : main.py

Version : 1.1.1
"""

from colorama import Fore

def print_khayyam_triangle(rows):
    for i in range(rows):
        num = 1
        for j in range(1, i+2):
            print(num, end=' ')
            num = int(num * (i - j + 1) / j)
        print()

try:
    rows = int(input(f"{Fore.GREEN}Rows >>> {Fore.CYAN}"))
except ValueError:
    print(f"{Fore.RED} Error: Value Error")

print_khayyam_triangle(rows)