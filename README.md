# Final project for 2023's 219114/115 Programming I
* Starting files for part 1
  - database.py
  - project_manage.py
  - persons.csv

# List of files in the final project repo

1. project_handler.py
    - Is written in procedural code. The main purpose of it is to be link between each modules and class to work together.
2. database.py
    - Class DB - contain the tools to create a database to contain every datas.
    - Class Table - Use to get data out of the database and perform selection and filter on data.
    - Class Csv_reader - A tool to easily read data from csv file.
3. database_handler.py
    - Class DB - Works similarly to class DB from the previous file. But this Db class can easily save table datas into csv file. This class is essential to my project because I use a lot of modules in a seperate file, so normal DB is harder to deal with here.
    - Class Get_person_id - Is use to get person's id from their name.
4. frame.py
    - Class Frame - Used to display text nicely in a frame.
5. notification_handler.py
    - Class Invite - Used to handle request involving invitation of any kind and submiting work.
6. person_handler.py
    - Class Person - A parent class for the following class. Also provide you with a basic information of a person such as id and name.
    - Class Student - Containing every action that a student can do. Is a child class of Person class.
    - Class Lead - Containing every action that a lead can do. Is a child class of Person class.
    - Class Member - Containing every action that a member can do. Is a child class of Person class.
    - Class Faculty - Containing every action that a faculty can do. Is a child class of Person class.
    - Class Admin - Containing every action that a admin can do. Is a child class of Person class.
7. project_handler.py
    - Class Project - perform every action related to a project eg. change name or add advisor

# Usage

Run the following command:
```bash
python project_manage.py
```

# Action that can be performed

<table>
    <tr>
      <td>Role</td><td>Action</td><td>Method</td><td>Class</td><td>Completion percentage</td>
    </tr>
    <td>
      <td>Student</td><td>manage incoming invitation</td><td>manage_incoming_invitation</td><td>Student</td><td>100%</td>
    </tr>
    
</table>

# Missing features and bugs

1. The Admin's code hasn't been completed at all.
2. An advisor might not be able to join multiple projects.
3. The feature evaluating project where 3 outsider evaluate the project to determine the fate of the project at the end is not implemented.
