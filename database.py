# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file

import csv, os, copy

class CSV_reader():
    def __init__(self):
        self.__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        
    def read_data_from_file(self, file_name):
        """
        :param: file_name : file's name
        :return: a list of a datas in the csv file specified.
        """
        data = []
        with open(os.path.join(self.__location__, file_name)) as f:
            rows = csv.DictReader(f)
            for r in rows:
                data.append(dict(r))
        return data



# add in code for a Database class
class DB:
    def __init__(self):
        self.__database = []

    def insert(self, table):
        self.__database.append(table)

    def delete(self, table_name):
        for table_num in range(len(self.__database)):
            if self.__database[table_num].table_name == table_name:
                self.__database.pop(table_num)
                return 1
        return None

    def search(self, table_name):
        for table in self.__database:
            if table.table_name == table_name:
                return table
        return None
    
    @property
    def database(self):
        return self.__database
    

# add in code for a Table class
import copy
class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table
    
    def join(self, other_table, common_key):
        joined_table = Table(self.table_name + '_joins_' + other_table.table_name, [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table
    
    def filter(self, condition):
        filtered_table = Table(self.table_name + '_filtered', [])
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table
    
    def aggregate(self, function, aggregation_key):
        temps = []
        for item1 in self.table:
            temps.append(float(item1[aggregation_key]))
        return function(temps)
    
    def select(self, attributes_list):
        temps = []
        for item1 in self.table:
            dict_temp = {}
            for key in item1:
                if key in attributes_list:
                    dict_temp[key] = item1[key]
            temps.append(dict_temp)
        return temps
    
    def add(self, _list):
        if not isinstance(_list, (list)):
            raise TypeError("_list param must be a list.")
        for i in _list:
            if not isinstance(i, (dict)):
                raise TypeError("One of item is _list is not a dict.")
        self.table += _list

    def __str__(self):
        return self.table_name + ':' + str(self.table)

# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary
