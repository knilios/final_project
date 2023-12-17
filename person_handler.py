import database
import frame
import database_handler
import project_handler
import notification_handler

invite = notification_handler.Invite()
main_frame = frame.Frame("main")
main_frame.add_header("WELCOME! \n")
persons_table = database_handler.DB('persons')

class Person:
    def __init__(self, person_id):
        # if not isinstance(db, database.DB):
        #     raise TypeError("db must be a DB class.")
        persons = persons_table.get_table() # db.search("persons")
        if person_id not in list(map(lambda x: x['ID'], persons.select(['ID']))):
            raise ValueError("Cannot find a person with that id.")
        selected = persons.filter(lambda x: x["ID"] == person_id).select(['first', 'last', 'type'])
        print(selected)
        self.__firstname = selected[0]['first']
        self.__lastname = selected[0]['last']
        self.__type = selected[0]['type']
        self._id = person_id
        self.name = self.__firstname + " " + self.__lastname
        

    def get_id(self):
        return self._id
       
        
class Student(Person):
    def __init___(self, person_id):
        super(Student, self).__init__(person_id)
        
    def manage_incoming_invitation(self):
        _invite_list = invite.get_invite_member(self._id)
        if _invite_list == []:
            main_frame.add("You have no invite yet.")
            main_frame.display()
            main_frame.clear()
            input("Press enter to exit...")
            return
        else:
            main_frame.add("These are your invitations: /n")
            for i in range(len(_invite_list)):
                _p = project_handler.Project_handler(_invite_list[i]["project_id"])
                main_frame.add(f"Type {i+1} to manage project {_p.name}.")
        main_frame.add("Type 'exit' to exit this session.")
        main_frame.display()
        main_frame.clear()
        while True:
            num = input("Please type your project of choice: ")
            if num == 'exit':
                return
            try:
                int(num)
            except ValueError:
                continue
            if int(num)-1 not in range(len(_invite_list)):
                continue
            manage_choice = input("Enter 0 to join, enter 1 to reject the offer. Enter anything else to exit: ")
            if manage_choice == 0:
                _project = project_handler.Project_handler(_invite_list[int(num)-1]["project_id"])
                invite.accept_invite_member(_invite_list[int(num)-1]["invite_id"])
                _project.change_role(self._id, "member")
                break
            elif manage_choice == 1:
                invite.reject_invite_member(_invite_list[int(num)-1]["invite_id"])
                break
            else:
                continue
            
    def create_a_project(self):
        name = input("Please enter the project name: ")
        _project = project_handler.Project(name, self._id)
        _project.change_role(self._id, "lead")


class Lead(Person):
    def __init___(self, person_id):
        super().__init__(person_id)
        self._id = person_id
        self.__project = project_handler.Project_handler(person_id, True)
        
    def see_project_status(self):
        """
        see pending memeber, pending advisor and read to solicit an advisor
        """
        main_frame.add("Project's status: \n")
        main_frame.add("Pending members: ")
        pending = invite.get_invite_project(self.__project.id)
        if len(pending[0]) == 0 or pending[1] == {}:
            main_frame.add("BLANK")
        else:
            for i in pending[0]:
                main_frame.add(f"{Person(i['receiver_id']).name} : {i['respond']}")
        main_frame.add("\nPending advisors: ")
        if len(pending[1]) == 0 or pending[1] == {}:
            main_frame.add("BLANK")
        else:
            for i in pending[1]:
                main_frame.add(f"{Person(i['receiver_id']).name} : {i['respond']}")
        main_frame.add("\nAdvisor solicitability:")
        if self.__project.member[0] != 'none':
            main_frame.add("YES")
        else:
            main_frame.add("NO")
        main_frame.display()
        main_frame.clear()
        input("Press enter to exit...")

    def manage_project_information(self):
        """
        See project's name and id, allowing to change name
        """
        main_frame.add("Project's information \n")
        main_frame.add(f"Name: {self.__project.name}")
        main_frame.add(f"ID: {self.__project.id}")
        main_frame.display()
        main_frame.clear()
        choice = input("Would you like to change the project's name? Type 'y' if yes, type anything else to exit: ")
        if choice == 'y':
            try:
                name = input("Enter your new project's name here: ")
                self.__project.name = name
                print("Done")
                input("Press Enter...")
                return
            except ValueError:
                print("Invalid input.")
                input("Press enter...")
                return
        return

    def send_a_member_invitation(self):
        if self.__project.member[1] != 'none':
            main_frame.add("Cannot add anymore member.")
            main_frame.display()
            main_frame.clear()
            input("Press enter to proceed...")
        main_frame.add("Please select the person to send invite to.")
        main_frame.display()
        main_frame.clear()
        input("Press enter to proceed...")
        member_id = database_handler.Get_person_id().ui("student")
        invite.send_invite_member(self.__project.id, member_id)
        main_frame.add("Invited")
        main_frame.display()
        main_frame.clear()
        input("Press enter to proceed...")
        
    def send_an_advisor_invitation(self):
        """
        can only do after 2 members are already there
        """
        if self.__project.member[1] == "none":
            print("Cannot invite an advisor yet")
            input("Press enter to exit.")
        main_frame.add("Please select a faculty member to send invite to.")
        main_frame.display()
        main_frame.clear()
        input("Press enter to proceed...")
        member_id = database_handler.Get_person_id().ui("faculty", 'advisor')
        invite.send_invite_member(self.__project.id, member_id)
        main_frame.add("Invited")
        main_frame.display()
        main_frame.clear()
        input("Press enter to proceed...")

    def submit_work(self):
        _type = input("Please Enter a type of work: ")
        message = input("Please enter your link to your work file")
        invite.send_work(self.__project.id, self.__project.advisor, _type, message)
        input("You work has been submitted, press enter to proceed.")
        
        
class Member(Person):
    def __init___(self, person_id):
        super().__init__(person_id)
        self._id = person_id
        self.__project = project_handler.Project_handler(person_id, True)
    
    def see_project_status(self):
        """
        see pending member and advisor
        """
        main_frame.add("Project's status: \n")
        main_frame.add("Pending members: ")
        pending = invite.get_invite_project(self.__project.id)
        if len(pending[0]) == 0 or pending[1] == {}:
            main_frame.add("BLANK")
        else:
            for i in pending[0]:
                main_frame.add(f"{Person(i['receiver_id']).name} : {i['respond']}")
        main_frame.add("\nPending advisors: ")
        if len(pending[1]) == 0 or pending[1] == {}:
            main_frame.add("BLANK")
        else:
            for i in pending[1]:
                main_frame.add(f"{Person(i['receiver_id']).name} : {i['respond']}")
        main_frame.add("\nAdvisor solicitability:")
        if self.__project.member[0] != 'none':
            main_frame.add("YES")
        else:
            main_frame.add("NO")
        main_frame.display()
        main_frame.clear()
        input("Press enter to exit...")
        
    def modify_project_information(self):
        """
        see and modify project's name
        """
        main_frame.add("Project's information \n")
        main_frame.add(f"Name: {self.__project.name}")
        main_frame.add(f"ID: {self.__project.id}")
        main_frame.display()
        main_frame.clear()
        choice = input("Would you like to change the project's name? Type 'y' if yes, type anything else to exit: ")
        if choice == 'y':
            try:
                name = input("Enter your new project's name here: ")
                self.__project.name = name
                print("Done")
                input("Press Enter...")
                return
            except ValueError:
                print("Invalid input.")
                input("Press enter...")
                return
        return
        
    def see_invitation_respondant(self):
        """
        See who responded back => see members
        """
        main_frame.add("Respondant:")
        main_frame.add("Member:")
        for i in self.__project.member:
            if i == 'non':
                continue
            main_frame.add(Person(i).name)
        main_frame.add("Advisor:")
        if self.__project.advisor != 'none':
            main_frame.add(Person(self.__project.advisor).name)
        input("Enter to exit...")
        

class Faculty(Person):
    def __init___(self, person_id):
        super().__init__(person_id)
        
    def manage_invitation(self):
        _invite_list = invite.get_invite_advisor(self._id)
        if _invite_list == []:
            main_frame.add("You have no invite yet.")
            main_frame.display()
            main_frame.clear()
            input("Press enter to exit...")
            return
        else:
            main_frame.add("These are your invitations: /n")
            for i in range(len(_invite_list)):
                _p = project_handler.Project_handler(_invite_list[i]["project_id"])
                main_frame.add(f"Type {i+1} to manage project {_p.name}.")
        main_frame.add("Type 'exit' to exit this session.")
        main_frame.display()
        main_frame.clear()
        while True:
            num = input("Please type your project of choice: ")
            if num == 'exit':
                return
            try:
                int(num)
            except ValueError:
                continue
            if int(num)-1 not in range(len(_invite_list)):
                continue
            manage_choice = input("Enter 0 to join, enter 1 to reject the offer. Enter anything else to exit: ")
            if manage_choice == 0:
                _project = project_handler.Project_handler(_invite_list[int(num)-1]["project_id"])
                invite.accept_invite_advisor(_invite_list[int(num)-1]["invite_id"])
                _project.change_role(self._id, "member")
                break
            elif manage_choice == 1:
                invite.reject_invite_advisor(_invite_list[int(num)-1]["invite_id"])
                break
            else:
                continue
        

class Advisor(Person):
    def __init___(self, person_id):
        super().__init__(person_id)
        self._id = person_id
        self.__project = project_handler.Project_handler(person_id, True)
        
    def view_and_edit_project_information(self):
        """
        See project's name and id, allowing to change name
        """
        main_frame.add("Project's information \n")
        main_frame.add(f"Name: {self.__project.name}")
        main_frame.add(f"ID: {self.__project.id}")
        main_frame.display()
        main_frame.clear()
        choice = input("Would you like to change the project's name? Type 'y' if yes, type anything else to exit: ")
        if choice == 'y':
            try:
                name = input("Enter your new project's name here: ")
                self.__project.name = name
                print("Done")
                input("Press Enter...")
                return
            except ValueError:
                print("Invalid input.")
                input("Press enter...")
                return
        return
        
    def manage_invitation(self):
        _invite_list = invite.get_invite_advisor(self._id)
        if _invite_list == []:
            main_frame.add("You have no invite yet.")
            main_frame.display()
            main_frame.clear()
            input("Press enter to exit...")
            return
        else:
            main_frame.add("These are your invitations: /n")
            for i in range(len(_invite_list)):
                _p = project_handler.Project_handler(_invite_list[i]["project_id"])
                main_frame.add(f"Type {i+1} to manage project {_p.name}.")
        main_frame.add("Type 'exit' to exit this session.")
        main_frame.display()
        main_frame.clear()
        while True:
            num = input("Please type your project of choice: ")
            if num == 'exit':
                return
            try:
                int(num)
            except ValueError:
                continue
            if int(num)-1 not in range(len(_invite_list)):
                continue
            manage_choice = input("Enter 0 to join, enter 1 to reject the offer. Enter anything else to exit: ")
            if manage_choice == 0:
                _project = project_handler.Project_handler(_invite_list[int(num)-1]["project_id"])
                invite.accept_invite_advisor(_invite_list[int(num)-1]["invite_id"])
                _project.change_role(self._id, "member")
                break
            elif manage_choice == 1:
                invite.reject_invite_advisor(_invite_list[int(num)-1]["invite_id"])
                break
            else:
                continue

    def evaluate_the_work(self):
        works = invite.get_work_project(self.__project.id)
        main_frame.add("Theses are the works submitted")
        for i in range(len(works)):
            main_frame.add(f'{i} : {works[i]["type"]}: {project_handler.Project_handler(works[i]["project_id"]).name} message:{works[i]["message"]}')
        main_frame.display()
        main_frame.clear()
        choice = input("Enter the choice you want to evaluate: ")
        while choice not in list(map(str, range(len(works)))):
            choice = input("Enter the choice you want to evaluate: ")
        eval_choice = ["pass", "fail"]
        evalu = input("Enter 0 for pass, 1 for fail.: ")
        while evalu not in ['0','1']:
            evalu = input("Enter 0 for pass, 1 for fail.: ")
        invite.mark_work(works[int(choice)]["work_id"], eval_choice[int(evalu)])
        
    # def resign_from_project(self):
    #     print("resign and find new advisor")

class Admin(Person):
    def __init__(self, person_id):
        super().__init__(person_id)

    def view_project_status(self):
        print("status")

    def manage_invitation(self):
        print("view and manage")

    def manage_members(self):
        print("person in the group")

    def view_databases_and_edit(self):
        print("database")




