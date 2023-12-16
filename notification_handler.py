import database_handler
import database
import project_handler
import person_handler
import time

invite_base = database_handler.DB("invites")
invite_table = invite_base.get_table()

class Invite:
    def __init__(self) -> None:
        pass

    def get_invite(self, self_id:str):
        invites = invite_table.filter(lambda x: x["receiver_id"] == self_id).select(['project_id'])
        return list(map(lambda x: x["project_id"], invites))

    def send_invite(self, project_id:str, receiver:str):
        invite_table.add([{"invite_id":str(int(round(time.time() * 1000))), "project_id": project_id, "receiver_id": receiver}])
        pass

    def accept_invite(self, invite_id:str, role:str):
        invite_data = invite_table.filter(lambda x: x[invite_id] == invite_id).select(["invite_id"])[0]
        if role == "student":
            project_handler.Project_handler(invite_data["invite_id"]).add_member(person_handler.Person(invite_data['receiver_id']))
        elif role == "faculty":
            project_handler.Project_handler(invite_data["invite_id"]).add_advisor(person_handler.Person(invite_data['receiver_id']))
        return None