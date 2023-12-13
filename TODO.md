# **TO-DO list**
- Student
    - See whether there is an incoming request from lead.
    - Accept or denied an incoming request
    - Create a project and become a lead themselves. 

- Lead
    - See all project's status
    - See and modify project's information.
    - See the respondant
    - Send out requests to the faculty member (can only be sent one at a time) and student to join their project.

- Member
    - See some of the project's status
    - See and modify project's information (with a notification to the project's lead about who changed what)
    - See who responded to the invitation

- Faculty
    - See lead's invitation
    - Can either confirm or deny the invitation.
    - Can become an advisor of any project

- Advisor
    - Can view the project's status
    - Can evaluate the project
    - Can either approve or deny the project
    - Can either accept or deny request from other projects.
    - Can resign from being a project advisor but the advisor has to send a request to another faculty member to become an advisor instead, and the advisor and only resign after the new advisor accepts the invite.

- Admin 
    - Can manage any table in the database.
    - Can delete any project
    - Can modify any project
    - Can modify the status of every person.
    - Can modify every person in any project.



Function and modules
1. Frame for better ui
2. notification handler
3. project handler
4. Chat system?


project class
1. name
2. lead
3. member
4. status
5. works
    - name of the work
    - date of submission
    - the work itself
    - comment from the advisor
6. Activity logs
7. Current invites

Actions on project
1. change name
2. change member, add, delete
3. change status
4. add work
5. add comment on works
6. Invite a member
7. Invite an advisor
8. Advisor leaves the project
9. Project Chat
10. Activity logs


Person type *Deprecated
1. Faculty
    - can become consultant
    - projects
2. Student
    - Can become lead or member
    - project in reposibility
3. Admin
    - I am da admin

Person handler - an inheritance of Person class

Actions on databases
1. add tables
2. delete tables
3. edit tables
4. view databases with gui if possible

Databases
1. login
2. person
3. Project id and user id relation
    id, project_id
4. Project details
5. Chat database?

Chat display ui?




what I did for 12/13/2023
    1. Added base classes for the project to based on
        - person handler classes
        - frame class
        - project handler classes
    2. Added one more csv file called project.csv to save all the project records

    what still left to do:
        1. finish the project handler class
        2. modify table class to be able to delete stuffs and easier to use in this context