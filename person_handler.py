import database
import frame

main_frame = frame.Frame("main")
main_frame.add_header("WELCOME TO FUNCTIONS! \n")

class Person:
    def __init__(self, person_id, db):
        if not isinstance(db, database.DB):
            raise TypeError("db must be a DB class.")
        persons = db.search("persons")
        if person_id not in list(map(lambda x: x['ID'], persons.select(['ID']))):
            raise ValueError("Cannot find a person with that id.")
        selected = persons.filter(lambda x: x["ID"] == person_id).select(['first', 'last', 'type'])
        print(selected)
        self.__firstname = selected[0]['first']
        self.__lastname = selected[0]['last']
        self.__type = selected[0]['type']
        self.__id = person_id
        self.name = self.__firstname + " " + self.__lastname
       
        
class Student(Person):
    def __init___(self, person_id, db):
        super().__init__(person_Id, db)
        
    def accept_incoming_req(self):
        main_frame.add("YAY")
        main_frame.display()
        main_frame.clear()
        input("Press enter to continue...")
        
    def create_a_project(self):
        print("created!")
        input("Press enter to continue...")
        
    def chat(self):
        print("Chatting")
        input("Press enter to continue...")
        

class Lead:
    def __init___(self, person_id, db):
        super().__init__(person_Id, db)
        
    def see_project_stat(self):
        print("stat")
        
    def send_member_invitation(self):
        print("inviting")
        
    def send_member_invitation(self):
        print("inviting")