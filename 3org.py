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

__version__ = '0.0+7b6b0d1.ninjas.unmerged'
__all__ = ['Resource', 'ConsumableResource', 'Location', 'Account']
ABOUT = """3org
Version 0.0 (7b6b0d1.ninjas.unmerged)
committed 2 May 2022"""

def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def home():
    cls()
    print('3org 0.0+7b6b0d1.main\n')
    print('Select one of the following to continue:')
    print('[P]eople')
    print('[R]esources')
    print('[A]ctivities')
    print('[S]ettings')
    print('[Q]uit')

    choice = input('3org> ').lower()

    # Not implemented yet
    if choice.startswith('p'):
        pass
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
        cls()

def main():
    print(ABOUT)
    print("\nPress RETURN to continue")
    input()
    home()

if __name__ == "__main__":
    main()
