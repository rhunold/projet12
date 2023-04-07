# EpicEvents

Epic Events is a company specialized in managing events for their clients.
Epic Events Employees use a CRM.

Each Employee have specific permissions based on their tasks

Admin can access [the admi](http://127.0.0.1:8000/admin), [the Web browsable API](http://127.0.0.1:8000/api/login/) or use the endpoints with Postman to to :
- create, view, modify and delete Employees, Clients, Contracts and Events
- Modify each Group permissions

Managers can access [the admi](http://127.0.0.1:8000/admin), [the Web browsable API](http://127.0.0.1:8000/api/login/) or use the endpoints with Postman to to :
- create, view, modify and delete Employees (he can create another manager but can not modify it)
- give permission to Employee depending on their department
- create, view, modify and delete Clients
- create, view, modify and delete Contracts
- create, view, modify and delete Events

Sales people can access [the Web browsable API](http://127.0.0.1:8000/api/login/) or use the endpoints with Postman to :
- view Employees, Clients and Events
- create and view every Clients
- modify and delete the Clients they are assigned
- create and view every Contracts
- modify and delete the Contracts they are assigned
- create Events

Support people can access [the Web browsable API](http://127.0.0.1:8000/api/login/) or use the endpoints with Postman to :
- view Employees and Clients
- view, modify and delete the Events they are assigned



This CRM is built on Django and Django Rest Framework


## Installation


### Clone this repository
``` 
git clone https://github.com/rhunold/projet12.git
```

### Create an environment at the root of the project
``` 
python3 -m venv env
```

### Activate the environment
``` 
source env/bin/activate
```

### Install pip
``` 
python3 -m pip install 
```

### If Postgress not installed yet on your system

[Install Postgress](https://www.postgresql.org/download/) if not installed yet.


Then open the app and create an admin user in "Login/Group Roles" with a right click > Create > Login/Group Role...
- In the field "name" : epic_events_admin


Then create a database.
1) On the "Databases", right click > Create > Database
2) On the Database field = 'epic_events_db'
3) On the Owner, select the epic_events_admin that you created
4) At the end, it will you ask a password = 'epic_events_admin_pass'



Be sur to have postgress in your path before installing psycopg2 : 
``` 
export PATH=/Library/PostgreSQL/Version/bin:$PATH
```

### Install the requirements
``` 
pip install -r requirements.txt
```

### Using the actual database

To use a database already used, you can make a dump of the sql files in the utilities folder

```
cd utilities/
psql -U epic_events_admin epic_events_db -h 127.0.0.1 < epic_events_db_postgresql.sql
```



You can log after you run the server (see next 'Run server' instructions below.)
#### Access of the actual database
| typeUser | email | password | user_id 
|-|-|-|-|
| SuperUser | admin@epicsevents.com | pwd_admin_epicsevents | 1
| Manager | manager1@epicsevents.com | man_epic_pwd | 3
| Manager | manager2@epicsevents.com | man_epic_pwd | 8
| Sale | sale1@epicsevents.com | sale_epic_pwd | 4
| Sale | sale2@epicsevents.com | sale_epic_pwd | 5
| Support | support1@epicsevents.com | sup_epic_pwd | 6
| Support | support2@epicsevents.com | sup_epic_pwd | 7

| None | test@epicsevents.com | test_epic_pwd | 9

| None | test2@epicsevents.com | test_epic_pwd | 12





#### Make migrations
```
python3 manage.py makemigrations api
```

#### Migrate
```
python3 manage.py migrate
```

Database is created.

You can create a superuser
```
python3 manage.py createsuperuser
```

## Run server

After environment is launch, use this command line to start the server
```
python3  manage.py runserver
```

Server adress : [http://127.0.0.1:8000](http://127.0.0.1:8000)



## API documentation
On [Postman](https://documenter.getpostman.com/view/25526925/2s93RZNq8K) you can see all the endpoints and the documentation.


## Other things about this project
This project use the module flake8 to respect pep8 guideline.
To test it by yourself, go to the root of the project and use this command line to generate a html file in the flake8 folder.
```
flake8 softdesk --format=html --htmldir=flake8-report --max-line-length=120 --exclude=migrations
```

To test with line command without generating a html report
```
flake8 crm --max-line-length=120 --exclude=migrations
```

