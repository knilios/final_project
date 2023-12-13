import os

class Frame:
    def __init__(self, name="untitled"):
        self.__name = name
        self.__components = []
        self.__header = []
        self.__footer = []
    
    def add_footer(self, text, name = "unnamed"):
        for i in self.__footer:
            if name in i:
                raise ValueError("name already existed")
        self.__footer.append({"name":name, "text":text})
        
    def delete_footer(self, name):
        for i in range(len(self.__footer)):
            if name in self.__footer[i]['name']:
                self.__footer.pop(i)
                return
        raise ValueError("name not found")
    
    def add_header(self, text, name = "unnamed"):
        for i in self.__header:
            if name in i:
                raise ValueError("name already existed")
        self.__header.append({"name":name, "text":text})
        
    def delete_header(self, name):
        for i in range(len(self.__header)):
            if name in self.__header[i]['name']:
                self.__header.pop(i)
                return
        raise ValueError("name not found")
    
    def add(self, text, name = "unnamed"):
        for i in self.__components:
            if name in i:
                raise ValueError("name already existed")
        self.__components.append({"name":name, "text":text})
        
    def delete(self, name):
        for i in range(len(self.__components)):
            if name in self.__components[i]['name']:
                self.__components.pop(i)
                return
        raise ValueError("name not found")
    
    def clear(self):
        self.__components = []
        
    def display(self):
        if self.__components == []:
            return -1
        os.system('cls' if os.name == 'nt' else 'clear')
        print("====================================================================================")
        if self.__header != []:
            for i in self.__header:
                print(i["text"])
        for i in self.__components:
            print(i["text"])
        if self.__footer != []:
            for i in self.__footer:
                print(i["text"])
        print("====================================================================================")
        

# Test codes
# frame1 = Frame("Nihao")
# frame1.add("name1", "This is the things")
# frame1.add("name2", "This is the second thing")
# frame1.add("name3", "This is the third thing")
# frame1.display()
# _name = input("Enter your name: ")
# frame1.delete("name2")
# frame1.add("ahh", f"Your name is {_name}")
# frame1.display()