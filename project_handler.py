import datetime
import person_handler
import database
import frame

class Project:
    def __init__(self, name, lead_id, member=[], status="unfinished", works=[], activity_logs=[f"Project created by {lead_id} at {datetime.datetime.now()}"], current_invites, db):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(lead_id, str):
            raise TypeError("lead_id must be a string")
        if not isinstance(status, str):
            raise TypeError("status must be a string")
        if not isinstance(works, list):
            raise TypeError("works must be a list")
        if not isinstance(activity_logs, list):
            raise TypeError("activity_logs must be a list")
        if not isinstance(current_invites, list):
            raise TypeError("current_invites must be a list")
        if not isinstance(db, database.Database):
            raise TypeError("current_invites must be a database object")
        if name.replace(" ", "") == "":
            raise ValueError("Please come up with a proper name!")
        
        self.__name = name
        self.__lead = person_handler.Lead(lead_id, db)
        self.__member = member
        self.__status = status
        self.__works = works
        self.__activity_logs = activity_logs.replace(lead_id, self.__lead.name)
        self.__current_invites = current_invites
        
        table = db.search("person")
        table.add([{'name':self.__name, 
                    'lead':self.__lead, 
                    'member':self.__member, 
                    'status':self.__member, 
                    'works':self.__works, 
                    'activitiy_logs':self.__activity_logs, 
                    'current_invites':self.__current_invites
                    }])
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name, person):
        if not isinstance(new_name, str):
            raise TypeError("new name must be a string")
        if new_name.replace(" ", "") == "":
            raise ValueError("Please come up with a proper name!")
        if not isinstance(person, (person_handler.Lead, person_handler.Member, person_handler.Advisor)):
            raise TypeError("person must only be a person involved in the project.")
        self.__activity_logs.append(f"Name changed from {self.__name} to {new_name} by {person.name}")
        self.__name = new_name
        
    def add_member(self, new_person):
        if not isinstance(person, person_handler.Member):
            raise TypeError("person must be a member only")
        if len(self.__member) >= 2:
            raise ValueError("This group is full")
        self.__member.append(new_person)
        
    def add_work(self, name, description, work):
        return
    
    def invite_member(self, person_id):
        return 
    
    def invite_advisor(self, person_id):
        return
    
    def remove_advisor(self):
        return
    
    def remove_member(self, member_id, person_id)
        return
    
    def get_activity_logs(self):
        return
        
        
        