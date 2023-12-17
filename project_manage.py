# import database module
import database
from random import randint
import sys
import csv
import person_handler
import frame

# define a funcion called initializing

def add_user(_list): # person_id, first, last, password, role
    """
    Sorry, I defined more functions than specified
    """
    password = randint(1000,9999)
    role = ""
    if _list[3] == 'student':
        role = "member"
    elif _list[3] == 'faculty':
        role = 'faculty'
    else:
        role = 'admin'
    return {'ID':_list[0], 'username':f"{_list[1]}.{_list[2][0:1]}", 'password':str(password), 'role':role}

def initializing():
    reader = database.CSV_reader()
    persons_data = reader.read_data_from_file("persons.csv")
    login_data = reader.read_data_from_file("login.csv")
    project_data = reader.read_data_from_file("project.csv")
    persons = database.Table('persons', persons_data)
    login_table = database.Table('login', login_data)
    project_table = database.Table('project', project_data)
    global database_main
    database_main = database.DB()
    database_main.insert(persons)
    data =[]
    # # load database
    # result = []
    # for i in persons_data:
    #     result.append(add_user(list(i.values())))
    # login_table = database.Table('login', result)
    # print(login_table)
    database_main.insert(login_table)
    database_main.insert(project_table)

# here are things to do in this function:

    # create an object to read all csv files that will serve as a persistent state for this program

    # create all the corresponding tables for those csv files

    # see the guide how many tables are needed

    # add all these tables to the database


# define a funcion called login

def login():
    global username
    global password
    username = input('Enter username: ')
    password = input('Enter password: ')
    login_table = database_main.search('login')
    persons = login_table.select(['ID', 'username', 'password', 'role'])
    for i in persons:
        if i['username'] == username:
            if i['password'] == password:
                print(i)
                return i['ID'], i['role']
    return None

def login_clone():
    login_table = database_main.search('login')
    persons = login_table.select(['ID', 'username', 'password', 'role'])
    for i in persons:
        if i['username'] == username:
            if i['password'] == password:
                print(i)
                return i['ID'], i['role']
    return None
    

# here are things to do in this function:
   # add code that performs a login task
        # ask a user for a username and password
        # returns [ID, role] if valid, otherwise returning None

def save_csv(name, content):
    myFile = open(f'{name}.csv', 'w')
    writer = csv.writer(myFile)
    writer.writerow(content[0].keys())
    for dictionary in content:
        writer.writerow(dictionary.values())
    myFile.close()

# define a function called exit
def exit():
    # loop in every table in database
    for table in database_main.database:
        # save the file
        save_csv(table.table_name, database_main.search(table.table_name).table)
    sys.exit()

# make calls to the initializing and login functions defined above

initializing()
val = login()

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id
while True:
    if val == None:
        print("invalid username or wrong password.")
        sys.exit()

    if val[1] == 'admin':
      # see and do admin related activities
      print("ah")

    elif val[1] == 'student':
        student = person_handler.Student(val[0])
        _list_function = []
        for i in dir(student):
            if (not i.startswith("_")) and (i != "name"):
                _list_function.append(i)
        student_frame = frame.Frame("student")
        student_frame.add(f"WELCOME {student.name}! Let's do some work, shall we?")
        student_frame.add("\nHere's what you can do: ")
        for i in range(len(_list_function)):
            student_frame.add(f"    type {i+1} for {_list_function[i]}")
        student_frame.display()
        i = input("Choose your action: ")
        if i == "exit":
            sys.exit() # change to exit function later
        try:
            int(i)
        except ValueError:
            continue
        if (int(i) -1) not in range(len(_list_function)):
            i = input("Choose your action: ")
            if i == "exit":
                sys.exit() # change to exit function later
        getattr(student, _list_function[int(i)-1])()

    # elif val[1] == 'member':
    #   # see and do member related activities
    # elif val[1] == 'lead':
    #   # see and do lead related activities
    # elif val[1] == 'faculty':
    #   # see and do faculty related activities
    # elif val[1] == 'advisor':
    #     # see and do advisor related activities

    # once everyhthing is done, make a call to the exit function
    exit()
