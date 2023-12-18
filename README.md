# Final project for 2023's 219114/115 Programming I
* Starting files for part 1
  - database.py
  - project_manage.py
  - persons.csv

# List of files and classes in the final project repo

1. project_handler.py
    - Is written in procedural code. The main purpose of it is to be link between each modules and class to work together.
    - Functions in this file:
      - login - get username and password from the user and then determine their role and id.
      - login_clone - use username and password acquired from login function to determind user's role and id.
      - initializing - initialize essential tools for login process.
      - add_user - generate a random pass word and organize data to be save into a generated login.csv file.
      - exit - A function to exit the program. It saves all the table in the database into a file. But it is not used here because I used a different method to save data into csv files due to modules complications (I have a lot of module files).

2. database.py
    - Class DB - contain the tools to create a database to contain every datas.
    - Class Table - Use to get data out of the database and perform selection and filter on data.
    - Class Csv_reader - A tool to easily read data from a csv file.

3. database_handler.py
    - Class DB - Works similarly to class DB from the previous file. But this Db class can easily save table datas into csv file. This class is essential to my project because I use a lot of modules in a seperate file, so normal DB is harder to deal with here.
    - Class Get_person_id - Is use to get person's id from their name.

4. frame.py
    - Class Frame - Used to display texts nicely in a frame.

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

8. advisor_pending_request.csv
    - This csv contains datas of pending request to faculty members.

9. invites.csv
    - Does nothing at the moment

10. login.csv
    - store username and password of users, use to login and identify the user.

11. member_pending_request.csv
    - Store request datas to student user.

12. person.csv
    - Does nothing at the moment
13. persons.csv
    - Store data of each user, it is the most essential file in the system because it was the starting point file. The program will fetch datas from this file to run and create other csv files.

14. project.csv
    - Store data of projects.

15. work_notification.csv
    - Store data of works submitted to the advisors from each project.
16. PROPOSAL.md
    - A file describing the evaluation process.
17. TODO.md
    - A file containing initial planning of the system and additional plannings afterwards.

# Usage

1. Run the following command:
```bash
git clone https://github.com/knilios/final_project.git
```
2. Delete all .csv files except login.csv and persons.csv
3. In persons.csv and login.csv, change all word 'lead' and 'member' to 'student' and change all word 'advisor' into 'faculty'.
4. Run the following command:
```bash
python project_manage.py
```

# Action that can be performed

Yes, the method are named accordingly to it's functionality.

| Role | Action | Method | Class | Completion percentage |
|------|--------|--------|-------|-----------------------|
| Student | manage incoming invitation | manage_incoming_invitation | Student | 100% |
| Student | create a project | create_a_project | Student | 100% |
| Lead | manage incoming invitation | manage_incoming_invitation | Lead | 100% |
| Lead | see project status | see_project_status | Lead | 100% |
| Lead | manage project information | manage_project_information | Lead | 100% |
| Lead | send a member invitation | send_a_member_invitation | Lead | 100% |
| Lead | submit work | submit_work | Lead | 100% |
| Member | see project status | see_project_status | Member | 100% |
| Member | modify project information | modify_project_information | Member | 100% |
| Member | see invitation respondent | see_invitation_respondant | Member | 100% |
| Faculty | manage invitation | manage_invitation | Faculty | 100% |
| Advisor | view and edit project information | view_and_edit_project_information | Advisor | 90% |
| Advisor | manage invitation | manage_invitation | Advisor | 70% |
| Advisor | evaluate the work | evaluate_the_work | Advisor | 90% |


# Missing features and bugs

1. The Admin's code hasn't been completed at all.
2. An advisor might not be able to join multiple projects.
3. The feature evaluating project where 3 outsider evaluate the project to determine the fate of the project at the end is not implemented.
4. The login.csv is not generating automatically.
5. Currently the system has no code for reseting itself, so to reset the system, manual file deletion and modification must be perform. 