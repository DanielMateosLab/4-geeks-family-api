
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = []

    # Generate unique random members ID's
    def _generateId(self):
        id = None
        def id_exists(id):
            return len([member for member in self._members if member["id"] == id]) > 0

        while id == None or id_exists(id):
            id = randint(0, 99999999)

        return randint(0, 99999999)

    #  Adds a new member to the family
    #  Assumes member has name (Str), age (Int), lucky_numbers ([Int])
    def add_member(self, member):
        self._members.append({
            "id": self._generateId(),
            "last_name": self.last_name,
            **member,
        })

    # Deletes the member with the given id
    def delete_member(self, id):
        self._members = [member for member in self._members if member["id"] != id]

    # Returns the member with the given id or None
    def get_member(self, id):
        member = None

        # We find the member with the given id
        try:
            member = [member for member in self._members if member["id"] == id][0]
        except IndexError:
            pass

        return member

    # Returns a list of all family members
    def get_all_members(self):
        return self._members
