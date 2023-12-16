import datetime
import person_handler
import database
import frame
import database_handler
import time
import person_handler
import notification_handler

get_id = database_handler.Get_person_id()
persons_table = database_handler.DB("person")
project = database_handler.DB("project")
project_table = project.get_table()
main_frame = frame.Frame()
invite = notification_handler.Invite()

class Project:
    def __init__(self, name, lead_id, current_invites, member=[], status="unfinished", works=[], activity_logs=[f"Project created by hahaha at {datetime.datetime.now().isoformat()}"], advisor = None, project_id = str(int(round(time.time() * 1000)))):
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
        if name.replace(" ", "") == "":
            raise ValueError("Please come up with a proper name!")
        # advisor must be a person class

        self.__name = name
        self.__lead = person_handler.Lead(lead_id)
        self.__member = string_to_list(member) # member => [member_id, member_id]
        self.__status = status
        self.__works = string_to_list(works)
        if len(activity_logs) == 1:
            self.__activity_logs = activity_logs[0].replace("hahaha", self.__lead.name)
        else:
            self.__activity_logs = string_to_list(activity_logs)
        self.__current_invites = string_to_list(current_invites)
        self.__advisor = advisor
        self.__id = str(project_id) # current time in ms
        
        # table = db.search("person")
        project_table.add([{'name':self.__name, 
                    'lead':lead_id, 
                    'member':list_to_string(self.__member), 
                    'status':list_to_string(self.__status), 
                    'works':list_to_string(self.__works), 
                    'activitiy_logs':list_to_string(self.__activity_logs), 
                    'current_invites':self.__current_invites,
                    "id":self.__id
                    }])
        project.overide_new_table(project_table)
        
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
        if not isinstance(new_person, person_handler.Person):
            raise TypeError("person must be a member only")
        if len(self.__member) >= 2:
            raise ValueError("This group is full")
        self.__member.append(new_person.get_id())
        
    def add_work(self, name, description, work, adder_id=None): 
        _list = {"name": name, "description": description, "work": work, "comment":[]}
        self.__works.append(_list)
        return
    
    def invite_member(self):
        if len(self.__member) >= 2:
            print("Cannot add more members.")
            return
        _id = get_id.ui("student")
        invite.send_invite(self.__id, _id)
    
    def invite_advisor(self):
        advisor_id = get_id.ui("faculty")
        invite.send_invite(self.__id, advisor_id)
    
    def add_advisor(self, new_advisor_id):
        """
        new_advisor must be an advisor class
        """
        new_advisor = person_handler.Advisor(new_advisor_id)
        self.__activity_logs.append(f"New advisor {new_advisor} has joined at {datetime.datetime.now().isoformat()}.")
        self.__advisor = new_advisor
        return
    
    def remove_advisor(self):
        self.__activity_logs.append(f"Advisor {self.__advisor} has left at {datetime.datetime.now().isoformat()}.")
        self.__advisor = ""
        return
    
    def remove_member(self, member_id, lead_id):
        if member_id not in self.__member:
            raise ValueError("member_id not found in this project")
        self.__activity_logs.append(f"{person_handler.Person(lead_id).name} removed {person_handler.Person(member_id).name} from the group at {datetime.datetime.now().isoformat()}.")
        self.__member.pop(self.__member.index(member_id))
        return
    
    def get_activity_logs(self):
        main_frame.add(f"Here are the activity logs for the project {self.__name}. /n")
        for i in self.__activity_logs:
            main_frame.add(i)
        main_frame.display()
        main_frame.clear()
        input("Press enter to exit...")
        return
        

class Project_handler(Project):
    """
    reload project that already existed into a project class
    """
    def __init__(self, project_id:str):
        info = project_table.filter(lambda x: x["id"] == project_id).select(["name","lead_id","member","status","works","activity_logs","current_invite","id"])[0]
        super().__init__(info["name"], info["lead_id"], info["current_invites"], info['member'], info['status'], info['works'], info['activity_logs'], info['adivisor'], project_id)

def list_to_string(s):
    str1 = ""
    for ele in s:
        str1 += ele + "///"
    return str1

def string_to_list(string):
    if isinstance(string, list):
        return string
    return string.split("///")

        