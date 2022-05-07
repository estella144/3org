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

__version__ = '0.0+7b6b0d1.ninjas.unmerged'
__all__ = ['replace_forbidden']

ABOUT = """replace_forbidden module for 3org
Version 0.0 (7b6b0d1.ninjas.unmerged)
committed 7 May 2022
Data version 0 (0x00000000)"""

def replace_forbidden(string):
    """Internal method to replace forbidden characters in string."""
    forbidden = ('\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06',
                 '\x07', '\x08', '\x09', '\x0A', '\x0B', '\x0C', '\x0D',
                 '\x0E', '\x0F', '\x10', '\x11', '\x12', '\x13', '\x14',
                 '\x15', '\x16', '\x17', '\x18', '\x19', '\x1A', '\x1B',
                 '\x1C', '\x1D', '\x1E', '\x1F', '<', '>', ':', '"',
                 '/', '\\', '|', '?', '*', '&')
    # Windows
    win_ffns = ('con', 'prn', 'aux', 'nul', 'com1', 'com2', 'com3',
                'com4', 'com5', 'com6', 'com7', 'com8', 'com9', 'lpt1',
                'lpt2', 'lpt3', 'lpt4', 'lpt5', 'lpt6', 'lpt7', 'lpt8',
                'lpt9')

    count = 0

    for i in string:
        if i in forbidden:
            string[count] = "_"
            count += 1

    del count

    for i in win_ffns:
        if string.startswith(i):
            string += "_"

    contains_only_spaces_and_periods = True

    for i in string:
        if i not in ('.', ' '):
            contains_only_spaces_and_periods = False

    if contains_only_spaces_and_periods:
        string += "_"

    return string
