
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

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        id = None
        def id_exists(id):
            return len([member for member in self._members if member.id == id]) > 0

        while id == None or id_exists(id):
            id = randint(0, 99999999)

        return randint(0, 99999999)

    # Assumes member has name (Str), age (Int), lucky_numbers ([Int])
    def add_member(self, member):
        self._members.append({
            "id": self._generateId(),
            "last_name": self.last_name,
            **member,
        })

    def delete_member(self, id):
        self._members = [member for member in self._members if member.id != id]

    def get_member(self, id):
        return next[
            # We find the member with the given id
            [member for member in self._members if member.id == id],
            # We set None as default to return it if no member is found
            None]

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
