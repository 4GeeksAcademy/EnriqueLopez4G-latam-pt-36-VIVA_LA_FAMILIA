
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
        self._next_id = 1

       # Lista de miembros inicial
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John Jackson",
                "age": 33,
                "Lucky Numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane Jackson",
                "age": 35,
                "Lucky Numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy Jackson",
                "age": 5,
                "Lucky Numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # fill this method and update the return
        # Generación de ID si no se proporciona uno
        member["id"] = member.get("id", self._generateId())        
        # Agregar el nuevo miembro a la lista de miembros
        self._members.append(member)
       
        return member, 200  # Retorna el miembro agregado y un código 200

    def delete_member(self, id):
        # Buscar el miembro por ID
        member_to_delete = None
        for member in self._members:
            if member["id"] == id:
                member_to_delete = member
                break

        if member_to_delete is None:
            # Si no se encuentra el miembro, retornar None (miembro no encontrado)
            return None

        # Eliminar el miembro de la lista
        self._members.remove(member_to_delete)
        return member_to_delete  # Retornar el miembro eliminado para confirmar la acción


    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
