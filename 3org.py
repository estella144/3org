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

from replace_forbidden import replace_forbidden as rp
import replace_forbidden
import person
import resource
from ansi import fg, bg
import ansi

__version__ = '0.0+72727bd.main'
ABOUT = """3org
Version 0.0 (72727bd.main)
committed 25 May 2022"""

cli_version = '''3org: version 0.0+72727bd.main
Platform: macOS 12.2.1 Intel (x86_64-i386) 64-bit
PyInstaller 5.1 (target: macOS-12.2.1-x86_64-i386-64bit)'''

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
    print(f'{fg.FAIL}[Q]uit{fg.ENDC}')

    choice = input('3org> ').lower()

    # Not implemented yet
    if choice.startswith('p'):
        people()
    elif choice.startswith('r'):
        pass
    elif choice.startswith('a'):
        pass
    elif choice.startswith('s'):
        settings()
    elif choice.startswith('q'):
        print("Are you sure you want to quit?")
        print("[Y/N] (default: no)")
        quit_choice = input("3org> ").lower()

        if quit_choice.startswith('y'):
            quit()
        else:
            home()
    else:
        input(f"{fg.FAIL}Unrecognized choice. Press ENTER to return\
        {fg.ENDC}")
        home()

def people():
    global __version__

    cls()
    print(f"3org {__version__}\n")
    print('[V]iew People')
    print('[A]dd Person')
    print('[B]ack to Home')
    print(f'{fg.FAIL}[Q]uit{fg.ENDC}')

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
        input(f"{fg.FAIL}Unrecognized choice. Press ENTER to return\
        {fg.ENDC}")
        people()

def settings():
    global __version__

    print(f"3org {__version__}\n")
    print("[A]bout")
    print("[G]eneral")
    print("[L]egal")
    print("[B]ack to Home")
    print(f"{fg.FAIL}[Q]uit{fg.ENDC}")

    choice = input("3org> ").lower()

    if choice.startswith('a'):
        settings_about()
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
        input(f"{fg.FAIL}Unrecognized choice. Press ENTER to return\
        {fg.ENDC}")
        settings()

def settings_about():
    global __version__

    print(ABOUT)
    print(ansi.ABOUT,"\n")
    print(person.ABOUT,"\n")
    print(replace_forbidden.ABOUT,"\n")
    print(resource.ABOUT,"n")
    input("Press ENTER to return to Settings...")
    settings()

def main():
    # System call to enable ANSI escape codes.
    os.system('')
    cls()
    print(ABOUT)
    print("\nPress RETURN to continue")
    input()
    home()

if __name__ == "__main__":
    main()
