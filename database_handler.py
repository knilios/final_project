"""
This file is used to handle all of the pesky database.py and the csv files

"""

import database
import sys
import csv
import frame as f

frame = f.Frame()

class DB:
    def __init__(self, file_name:str) -> None:
        """
        file name no need to add .csv
        """
        self.__file_name = file_name
        reader = database.CSV_reader()
        # might be an error of cannot find a file with that name
        try:
            self.__content = reader.read_data_from_file(f"{file_name}.csv")
        except FileNotFoundError:
            myFile = open(f'{file_name}.csv', 'w')
            writer = csv.writer(myFile)
            myFile.close()
            self.__content = reader.read_data_from_file(f"{file_name}.csv")
        pass

    def __save_csv(self):
        content = self.__content
        myFile = open(f'{self.__file_name}.csv', 'w')
        writer = csv.writer(myFile)
        writer.writerow(content[0].keys())
        for dictionary in content:
            writer.writerow(dictionary.values())
        myFile.close()

    def get_table(self):
        return database.Table(self.__file_name, self.__content)
    
    def overide_new_table(self, new_table:database.Table):
        self.__content = new_table.table
        self.__save_csv()


class Get_person_id:
    def __init__(self) -> None:
        self.__data = DB("persons").get_table()

    def get_by_name(self, _input, option = None, option2 = 'wasdwasdwasdwasd') -> list:
        try:
            if option == None:
                data = self.__data.filter(lambda x: _input in x["first"]+" "+x["last"]).select(["first", "last", "ID"])
            else:
                data = self.__data.filter(lambda x: x["type"] == option or option2 in x['type']).filter(lambda x: _input in x["first"]+" "+x["last"]).select(["first", "last", "ID"])
            _list = []
            for i in data:
                _list.append([i["first"] +" "+ i["last"], i["ID"]])
            return _list
        except KeyError:
            return []
    
    def ui(self, option = None, option2='wasdwasdwasdwasd') -> str:
        while True:
            frame.add("Enter the name of the person you are finding. Type 'exit' to exit the session.")
            frame.display()
            name = input("Enter here: ")
            if name == 'exit':
                break
            frame.clear()
            _list = self.get_by_name(name, option, option2)
            if _list == []:
                frame.add("Sorry, we cannot find the name that matched that input.")
                frame.display()
                frame.clear()
                continue
            frame.add("Here are the list of people you are looking for: /n")
            for i in range(len(_list)):
                frame.add(f"Enter {i+1} for {_list[i][0]}")
            _index = int(input("Enter the number: "))
            if _index-1 not in range(len(_list)):
                print("Invalid input!")
                input("Press enter to continue.")
                continue
            return _list[_index-1][1]
        
        

