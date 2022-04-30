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
import uuid

from replace_forbidden import replace_forbidden

__version__ = '0.0+3e6b701'
__all__ = ['Resource', 'ConsumableResource', 'Location']
ABOUT = """resource module for 3org
Version 0.0 (master@7f03b2f)
committed 30 April 2022
Data version 0 (0x00000000)"""

class Resource():
    """Representation of a resource."""

    def __init__(self, resource_type, name, description, location):
        # super(Resource, self).__init__()
        self.resource_type = resource_type
        self.name = name
        self.description = description
        self.location = location
        self.uuid = uuid.uuid1()

    def __str__(self):
        return f"Resource: {self.name} ({self.uuid.time_low})"

    def save(self):
        data = {name: self.name,
                resource_type: self.resource_type,
                description: self.description,
                location: self.location,
                uuid: str(self.uuid),
                data_version: 0}
        json.dump(open(f"data/people/{name}", "w"), data)

class ConsumableResource(Resource):
    """Subclass of Resource for (easily) consumable resources."""

    def __init__(self, resource_type, name, description, location,
                 expires=None):
        super(ConsumableResource, self).__init__()
        self.resource_type = "ConsumableResource"
        self.expires = expires
        # list of args to datetime.datetime in increasing granularity

    def __str__(self):
        return f"ConsumableResource: {self.name} ({self.uuid.time_low})"

    def __repr__(self):
        rep = f"ConsumableResource(resource_type, name, description,\n\
        expires)"
        return rep

class Location(Resource):
    """Subclass of Resource for locations, including storage containers."""

    def __init__(self, resource_type, name, description, location,
                 items=[]):
        super(Location, self).__init__()
        self.items = items

class Account(Resource):
    """Subclass of Resource for financial accounts."""

    def __init__(self, resource_type, name, description, location,
                 currency='GBP', balance=0):
        super(Account, self).__init__()
        self.balance = balance
