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

__version__ = '0.0'
__all__ = ['Person', 'load_person']

import json
import logging
import uuid

from replace_forbidden import replace_forbidden

class Person():
    """Representation of a person. (The creation of a new person is
    dealt with internally.)"""

    def __init__(self, name, description, org="No Organisation",
                 contacts={}, activities=[], uuid=uuid.uuid1()):
        super(Person, self).__init__()
        self.name = name
        self.description = description
        self.org = org
        self.contacts = contacts
        self.uuid = uuid

    def __str__(self):
        return self.name

    def save(self):
        data = {name: self.name,
                description: self.description,
                org: self.org,
                contacts: self.contacts,
                activities: self.activities,
                uuid: str(self.uuid)}
        json.dump(open(f"data/people/{name}", "w"), data)

    def add_contact(self, type, value):
        if type not in self.contacts:
            self.contacts.add(type, value)
        else:
            print("Failed to add field to contact: {type} already exists.")

def load_person(name):
    """Method to load a person from a file."""
    name = replace_forbidden(name)
    data = json.load(open(f"data/person/{name}", "r"))
    return Person(name=data.name, description=data.description,
                  org=data.org, contacts=data.contacts,
                  activities=data.activities, uuid=uuid.UUID(data.uuid))
