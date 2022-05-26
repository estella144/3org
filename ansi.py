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

import sys
import os

__version__ = '0.0+6f23b54.main'
ABOUT = """ansi module for 3org
Version 0.0 (6f23b54.main)
committed 26 May 2022"""

if 'idlelib.run' not in sys.modules:

    class fg:
        HEADER = '\033[95m' # Pink
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m' # Amber
        FAIL = '\033[91m' # Red
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    class bg:
        HEADER = '\x1b[6;30;45m' # Pink
        OKBLUE = '\x1b[6;30;44m'
        OKCYAN = '\x1b[6;30;46m'
        OKGREEN = '\x1b[6;30;42m'
        WARNING = '\x1b[6;30;43m' # Amber
        FAIL = '\x1b[6;30;41m' # Red
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

else:
    # ANSI color codes are not supported in IDLE mode.

    class fg:
        HEADER = ''
        OKBLUE = ''
        OKCYAN = ''
        OKGREEN = ''
        WARNING = ''
        FAIL = ''
        ENDC = ''
        BOLD = ''
        UNDERLINE = ''

    class bg:
        HEADER = ''
        OKBLUE = ''
        OKCYAN = ''
        OKGREEN = ''
        WARNING = ''
        FAIL = ''
        ENDC = ''
        BOLD = ''
        UNDERLINE = ''

if __name__ == "__main__":
    os.system("")
    print(f"{fg.FAIL}This module is not intended to be used directly!\n\
{fg.WARNING}Loading 3org.py...{fg.ENDC}")
    _3org = open('3org.py')
    program = _3org.read()
    exec(program)
