import database_handler
import database
import project_handler
import person_handler
import time

member_invite_base = database_handler.DB("member_pending_requrest")
advisor_invite_base = database_handler.DB("advisor_pending_request")
work_base = database_handler.DB("work_notification")
member_table = member_invite_base.get_table()
advisor_table = member_invite_base.get_table()
work_table = work_base.get_table()

class Invite:
    def __init__(self) -> None:
        pass

    def get_invite_project(self, project_id:str):
        member = member_table.filter(lambda x: x["project_id"] == project_id).select(["receiver_id", "respond"])
        advisor = advisor_table.filter(lambda x: x["project_id"] == project_id).select(["receiver_id", "respond"])
        return [member, advisor]

    def get_invite_member(self, self_id:str):
        invites = member_table.filter(lambda x: x["receiver_id"] == self_id).select(['project_id'])
        if member_table.filter(lambda x: x["receiver_id"] == self_id).table == []:
            return []
        else:
            return list(map(lambda x: x["project_id"], invites))

    def send_invite_member(self, project_id:str, receiver:str):
        member_table.add([{"invite_id":str(int(round(time.time() * 1000))), "project_id": project_id, "receiver_id": receiver, "respond":"pending", "res_date":"none"}])
        member_invite_base.overide_new_table(member_table)
        pass

    def accept_invite_member(self, invite_id:str):
        invite_data = member_table.filter(lambda x: x["invite_id"] == invite_id).select(["invite_id", "project_id", "receiver_id", "respond", "res_date"])
        invite_data[0]["respond"] = "accepted"
        _data = member_table.filter(lambda x: x["invite_id"] != invite_id and x['receiver_id'] == invite_data[0]["receiver_id"]).select(["invite_id", "project_id", "receiver_id", "respond", "res_date"])
        _data_new = []
        for i in _data:
            i["respond"] = "rejected"
            _data_new.append(i)
        invite_data += _data_new
        member_table.table = invite_data
        member_invite_base.overide_new_table(member_table)
        project_handler.Project_handler(invite_data[0]["invite_id"]).add_member(person_handler.Person(invite_data[0]['receiver_id']))
        return None
    
    def reject_invite_member(self, invite_id:str):
        invite_data = member_table.filter(lambda x: x["invite_id"] == invite_id).select(["invite_id", "project_id", "receiver_id", "respond", "res_date"])
        invite_data[0]["respond"] = "rejected"
        member_table.change_one_roll(member_table.filter(lambda x: x["invite_id"] == invite_id).select(["invite_id", "project_id", "receiver_id", "respond", "res_date"])[0], invite_data[0])
        member_invite_base.overide_new_table(member_table)
    
    def get_invite_advisor(self, self_id:str):
        invites = advisor_table.filter(lambda x: x["receiver_id"] == self_id).filter(lambda x: x["respond"] == "pending").select(['project_id'])
        if advisor_table.filter(lambda x: x["receiver_id"] == self_id).table == []:
            return []
        else:
            return list(map(lambda x: x["project_id"], invites))

    def send_invite_advisor(self, project_id:str, receiver:str):
        advisor_table.add([{"invite_id":str(int(round(time.time() * 1000))), "project_id": project_id, "receiver_id": receiver, "respond":"pending", "res_date":"none"}])
        advisor_invite_base.overide_new_table(advisor_table)
        pass

    def accept_invite_advisor(self, invite_id:str):
        invite_data = advisor_table.filter(lambda x: x["invite_id"] == invite_id).select(["invite_id", "project_id", "receiver_id", "respond", "res_date"])
        invite_data[0]["respond"] = "accepted"
        advisor_table.change_one_roll(advisor_table.filter(lambda x: x["invite_id"] == invite_id).select(["invite_id", "project_id", "receiver_id", "respond", "res_date"])[0], invite_data[0])
        member_invite_base.overide_new_table(advisor_table)
        project_handler.Project_handler(invite_data[0]["invite_id"]).add_advisor(invite_data[0]['receiver_id'])
        return None
    
    def reject_invite_advisor(self, invite_id:str):
        invite_data = advisor_table.filter(lambda x: x["invite_id"] == invite_id).select(["invite_id", "project_id", "receiver_id", "respond", "res_date"])
        invite_data[0]["respond"] = "rejected"
        advisor_table.change_one_roll(advisor_table.filter(lambda x: x["invite_id"] == invite_id).select(["invite_id", "project_id", "receiver_id", "respond", "res_date"])[0], invite_data[0])
        member_invite_base.overide_new_table(advisor_table)
        return None
    
    def send_work(self, project_id, receiver_id, _type, message):
        work_table.add([{"project_id": project_id, "receiver_id": receiver_id, "type": _type, "message":message, "status":"none", "work_id":str(int(round(time.time() * 1000)))}])
        work_base.overide_new_table(work_table)

    def get_work_advisor(self, _id):
        return work_table.filter(lambda x: x["receiver_id"] == _id and x["status"] == "none").select(["project_id", "receiver_id", "type", "message", "status", "work_id"])
        
    def get_work_project(self, _id):
        return work_table.filter(lambda x: x["project_id"] == _id).select(["project_id", "receiver_id", "type", "message", "status", "work_id"])
        
    def mark_work(self, work_id, status):
        work = work_table.filter(lambda x: x['work_id'] == work_id).select(["project_id", "receiver_id", "type", "message", "status", "work_id"])
        work[0]["status"] = status
        work_table.change_one_roll(work_table.filter(lambda x: x['work_id'] == work_id).select(["project_id", "receiver_id", "type", "message", "status", "work_id"])[0], work[0])
        work_base.overide_new_table(work_table)
