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
    def __init__(self, name, lead_id, member1='none', member2 = 'none', advisor='none', status="unfinished", project_id = str(int(round(time.time() * 1000))), old=False):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(lead_id, str):
            raise TypeError("lead_id must be a string")
        if not isinstance(status, str):
            raise TypeError("status must be a string")
        if name.replace(" ", "") == "":
            raise ValueError("Please come up with a proper name!")

        self.__name = name
        self.__lead = lead_id
        self.__member1 = member1
        self.__member2 = member2
        self.__status = status
        self.__advisor = advisor
        self.__id = str(project_id) # current time in ms
        
        # table = db.search("person")
        if not old:
            project_table.add([{'name':self.__name, 
                        'lead':self.__lead, 
                        'member1':self.__member1,
                        'member2':self.__member2, 
                        'status':self.__status, 
                        'advisor':self.__advisor,
                        "id":self.__id,
                        }])
            project.overide_new_table(project_table)
        
    @property
    def name(self):
        return self.__name
    
    @property
    def member(self):
        return [self.__member1, self.__member2]
    
    @property
    def advisor(self):
        return self.__advisor
    
    @property
    def status(self):
        return self.__status
    
    @property
    def id(self):
        return self.__id
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("new name must be a string")
        if new_name.replace(" ", "") == "":
            raise ValueError("Please come up with a proper name!")
        self.__name = new_name
        self.__update()
        
    def add_member(self, new_person):
        if not isinstance(new_person, (person_handler.Person, person_handler.Student)):
            raise TypeError("person must be a person or an student object only")
        if 'none' not in (self.__member1, self.__member2):
            raise ValueError("This group is full")
        if self.__member1 == "none":
            self.__member1 = new_person.get_id()
        else:
            self.__member2 = new_person.get_id()
        self.change_role(new_person.get_id(), "member")
        self.__update()
        
    def invite_member(self):
        if 'none' not in (self.__member1, self.__member2):
            print("Cannot add more members.")
            input("Press enter to proceed...")
            return
        _id = get_id.ui("student")
        invite.send_invite_member(self.__id, _id)
    
    def invite_advisor(self):
        advisor_id = get_id.ui("faculty")
        invite.send_invite_advisor(self.__id, advisor_id)
    
    def add_advisor(self, new_advisor_id):
        """
        new_advisor must be an advisor class
        """
        self.__advisor = new_advisor_id
        self.change_role(new_advisor_id, "advisor")
        self.__update()
        return
    
    def remove_advisor(self):
        self.change_role(self.__advisor, "faculty")
        self.__advisor = "none"
        self.__update()
        return
    
    def remove_member(self, member_id):
        if member_id not in (self.__member1, self.__member2):
            raise ValueError("member_id not found in this project")
        self.change_role(member_id, "student")
        if self.__member1 == member_id:
            self.__member1 = self.__member2
            self.__member2 = 'none'
        else:
            self.__member2 = 'none'
        self.__update()
        
        
    def change_role(self, person_id:str, new_role:str):
        logins = database_handler.DB("login")
        persons = database_handler.DB("persons")
        l_table = logins.get_table()
        p_table = persons.get_table()
        l = l_table.filter(lambda x: x["ID"] == person_id).select(['ID','username','password','role'])
        p = p_table.filter(lambda x: x["ID"] == person_id).select(['ID','first','last','type'])
        l[0]['role'] = new_role
        p[0]['type'] = new_role
        l_table.change_one_roll(l_table.filter(lambda x: x["ID"] == person_id).select(['ID','username','password','role'])[0], l[0])
        p_table.change_one_roll(p_table.filter(lambda x: x["ID"] == person_id).select(['ID','first','last','type'])[0], p[0])
        logins.overide_new_table(l_table)
        persons.overide_new_table(p_table)
        
    def __update(self):
        old = project_table.filter(lambda x: x["id"] == self.__id).select(["name","lead","member1","member2","status",'advisor',"id"])[0]
        project_table.change_one_roll(old, {'name':self.__name, 
                                            'lead':self.__lead, 
                                            'member1':self.__member1,
                                            'member2':self.__member2, 
                                            'status':self.__status, 
                                            'advisor':self.__advisor,
                                            "id":self.__id
                                            })
        project.overide_new_table(project_table)


class Project_handler(Project):
    """
    reload project that already existed into a project class
    """
    def __init__(self, project_id:str, is_person_id=False):
        _id = ""
        if is_person_id:
            _id = project_table.filter(lambda x: x["lead"] == project_id or x["member1"] == project_id  or x["member2"] == project_id or x['advisor'] == project_id).select(["id"])[0]["id"]
            project_id = _id
        info = project_table.filter(lambda x: x["id"] == project_id).select(["name","lead","member1","member2","status",'advisor',"id"])
        if len(info) > 1:
            f = frame.Frame()
            f.add("Please select the project:")
            for i in range(len(info)):
                f.add(f"{i+1} for project {info[i]['name']}")
            num = input("please select: ")
            while num not in list(map(str, range(len(info)))):
                num = input("please select: ")
            info = info[int(num)]
        else:
            info = info[0]
        super().__init__(info["name"], info["lead"], info['member1'], info['member2'], info['advisor'], info['status'], project_id, True)

def list_to_string(s):
    str1 = ""
    for ele in s:
        str1 += ele + "///"
    return str1

def string_to_list(string):
    if isinstance(string, list):
        return string
    return string.split("///")

        