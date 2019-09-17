#!/usr/bin/env python3
# 2 menu types. one allows you to select from different items,
# the other allows you to toggle different items 

import sys, os

def get_os():
    while True:
        os_type = ''
        print('1) win')
        print('2) nix')
        print('q) exit')
        choice = input("choose: ")
        if choice == 'q':
            print("Goodbye.")
            sys.exit(0)
        elif choice == '1':
            os_type = 'win'
            print('Windows Selected')
            return os_type
        elif choice == '2':
            os_type = 'nix'
            print("*nix Selected")
            return os_type
        else:
            redraw_screen('none')

def get_accounts_win():
    accts = [['madmin',True],['hadmin',True],['sadmin',False]]
    while True:
        print('1) madmin - ' + str(accts[0][1]))
        print('2) hadmin - ' + str(accts[1][1]))
        print('3) sadmin - ' + str(accts[2][1]))
        print('w) write')
        print("q) quit")
        choice = input("choose: ")
        if choice == 'q':
            print("Goodbye")
            sys.exit(0)
        elif choice == '1': #madmin
            accts[0][1] = not accts[0][1]
            redraw_screen('win')
        elif choice == '2': #hadmin
            accts[1][1] = not accts[1][1]
            redraw_screen('win')
        elif choice == '3': #sadmin
            accts[2][1] = not accts[2][1]
            redraw_screen('win')
        elif choice == 'w': #write changes
            return accts
        else:
            redraw_screen('win')
        
def get_accounts_nix():
    accts = [['root',True],['tomcat',False],["user3",False]]
    while True:
        print('1 root   - ' + str(accts[0][1]))
        print('2 tomcat - ' + str(accts[1][1]))
        print('3 user3  - ' + str(accts[2][1]))
        print('w write')
        choice = input("choose: ")
        if choice == 'q':
            sys.exit(0)
        elif choice == '1': #root
            accts[0][1] = not accts[0][1]
            redraw_screen('nix')
        elif choice == '2': #tomcat
            accts[1][1] = not accts[1][1]
            redraw_screen('nix')
        elif choice == '3': #user3
            accts[2][1] = not accts[2][1]
            redraw_screen('nix')
        elif choice == 'w': #write changes
            return accts
        else:
            redraw_screen('nix')

def redraw_screen(os_type):
    #os.system('cls')
    os.system('clear')
    if os_type == 'win':
        print('Windows Selected')
    elif os_type == 'nix':
        print('*nix Selected')
    elif os_type == 'none':
        print('Choose an OS...')
    else:
        print("ERROR")
        sys.exit(1)

def parse_accounts(accts):
    i=0
    acct_list = []
    for i in range(len(accts)):    
        if accts[i][1]:
            acct_list.append(accts[i][0])
    if len(acct_list) < 1:
        print("ERROR - no accounts selected")
        sys.exit(0)
    else:
        return acct_list  

redraw_screen('none')
os_type = get_os()
redraw_screen(os_type)
if os_type == 'win':
    accts = get_accounts_win()
elif os_type == 'nix':
    accts = get_accounts_nix()
else:
    print("ERROR - OS TYPE")
    sys.exit(0)
acct_list = parse_accounts(accts)