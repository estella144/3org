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

__version__ = '0.0+bf16aeb'
__all__ = ['Person', 'load_person']

ABOUT = """person module for 3org
Version 0.0 (master@bf16aeb)
committed 3 April 2022
Data version 0 (0x00000000)"""

import json
import logging
import logging.config
import uuid

from replace_forbidden import replace_forbidden

class Person():
    """Representation of a person. (The creation of a new person is
    dealt with internally.)"""

    def __init__(self, name, description, org="No Organisation",
        contacts={}, activities=[], uuid=uuid.uuid1()):
        print("Constructing Person, do not quit program.")
        logging.config.fileConfig('conf/logging_person.conf')
        # super(Person, self).__init__()
        init.info('Person constructor called.')
        self.name = name
        self.description = description
        self.org = org
        self.contacts = contacts
        self.uuid = uuid
        init.info(f'Person {uuid.time_low} constructed successfully. Saving.')
        print(f'Person {uuid.time_low} constructed successfully. Saving.')
        self.save()
        print(f'Person {uuid.time_low} saved successfully.')
        print(f'You may now quit the program without affecting this person.')

    def __str__(self):
        return f"Person: {self.name} ({self.uuid.time_low})"

    def save(self):
        print(f"Saving person {self.uuid.time_low} do not quit the program...")
        data = {name: self.name,
                description: self.description,
                org: self.org,
                contacts: self.contacts,
                activities: self.activities,
                uuid: str(self.uuid),
                data_version: 0}
        json.dump(open(f"data/people/{name}", "w"), data)

    def add_contact(self, type, value):
        if type not in self.contacts:
            self.contacts.add(type, value)
        else:
            print(f"Failed to add field to contact: {type} already exists.")

def load_person(name):
    """Method to load a person from a file."""

    data_versions_supported = [0]
    name = replace_forbidden(name)
    data = json.load(open(f"data/person/{name}", "r"))
    return Person(name=data.name, description=data.description,
                  org=data.org, contacts=data.contacts,
                  activities=data.activities, uuid=uuid.UUID(data.uuid))

if __name__ == "__main__":
    logging.config.fileConfig('conf/logging_person.conf')
    person.log('The program was called improperly from person. Loading main program.')
    print("This module is not intended to be used directly!/nLoading\
    3org.py...")
    exec("3org.py")
