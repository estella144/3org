# 3org, expenses tracker and organiser
# Copyright (C) 2022, Oliver Nguyen
#
# This file is part of 3org.
#
# 3org is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import datetime
import json
import logging
import logging.config
import os
import uuid

from replace_forbidden import replace_forbidden
import person
import resource

__version__ = '0.0+96fdfdb.ninjas.unmerged'
ABOUT = """3org
Version 0.0 (5c6056d.ninjas.unmerged)
committed 7 May 2022"""

def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def home():
    global __version__
    
    cls()
    print(f'3org {__version__}\n')
    print('Select one of the following to continue:')
    print('[P]eople')
    print('[R]esources')
    print('[A]ctivities')
    print('[S]ettings')
    print('[Q]uit')

    choice = input('3org> ').lower()

    # Not implemented yet
    if choice.startswith('p'):
        people()
    elif choice.startswith('r'):
        pass
    elif choice.startswith('a'):
        pass
    elif choice.startswith('s'):
        pass
    elif choice.startswith('q'):
        print("Are you sure you want to quit?")
        print("[Y/N] (default: no)")
        quit_choice = input("3org> ").lower()

        if quit_choice.startswith('y'):
            quit()
        else:
            home()
    else:
        input("Unrecognized choice. Press any key to return")
        home()

def people():
    global __version__

    cls()
    print(f"3org {__version__}\n")
    print('[V]iew People')
    print('[A]dd Person')
    print('[B]ack to Home')
    print('[Q]uit')
    
    choice = input('3org> ').lower()

    if choice.startswith('v'):
        pass
    elif choice.startswith('a'):
        pass
    elif choice.startswith('b'):
        home()
    elif choice.startswith('q'):
        print("Are you sure you want to quit?")
        print("[Y/N] (default: no)")
        quit_choice = input("3org> ").lower()

        if quit_choice.startswith('y'):
            quit()
        else:
            people()
    else:
        input("Unrecognized choice. Press any key to return")
        home()

def settings():
    print(f"3org {__version__}\n")
    print("[A]bout")
    print("[G]eneral")
    print("[L]egal")
    print("[B]ack to Home")
    print("[Q]uit")

    choice = input("3org> ").lower()

    if choice.startswith('a'):
        pass
    elif choice.startswith('g'):
        pass
    elif choice.startswith('l'):
        pass
    elif choice.startswith('b'):
        home()
    elif choice.startswith('q'):
        print("Are you sure you want to quit?")
        print("[Y/N] (default: no)")
        quit_choice = input("3org> ").lower()

        if quit_choice.startswith('y'):
            quit()
        else:
            settings()
    else:
        input("Unrecognized choice. Press any key to return")
        home()

def main():
    print(ABOUT)
    print("\nPress RETURN to continue")
    input()
    home()

if __name__ == "__main__":
    main()
