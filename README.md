# EpicEvents

Epic Events is a company specialized in managing events for their clients.
Epic Events Employees use a CRM.

Each Employee have specific permissions based on their tasks

Admin can access [the admin](http://127.0.0.1:8000/admin) to :
- create, view, modify and delete every Employees, Clients, Contracts and Events
- Modify each Group permissions

On the [the admin](http://127.0.0.1:8000/admin) Managers can :
- give permission to Employee depending on their department
- create, view, modify and delete Employee, Clients, Contracts and Events
- If a Manager create another manager,  he can not modify it, view it or delete it after it was created

Managers can access [the Web browsable API](http://127.0.0.1:8000/api/login/) or use the endpoints with [Postman](https://documenter.getpostman.com/view/25526925/2s93RZNq8K) to :
- create, view, modify and delete all Clients
- create, view, modify and delete all Contracts
- create, view, modify and delete all Events


Sales people can access [the Web browsable API](http://127.0.0.1:8000/api/login/) or use the endpoints with [Postman](https://documenter.getpostman.com/view/25526925/2s93RZNq8K) to :
- create a new Client or a new Contract
- view, modify or delete the Clients or Contract they are assigned
- create Events

Support people can access [the Web browsable API](http://127.0.0.1:8000/api/login/) or use the endpoints with [Postman](https://documenter.getpostman.com/view/25526925/2s93RZNq8K) to :
- view, modify and delete the Events they are assigned
- view Clients that are associated to the Events they are assigned


This CRM is built on Django and Django Rest Framework

## ERD

![ERD](utilities/ERD_Projet_12.png)


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
| None | test_a_supprimer@epicsevents.com | test_epic_pwd | 18


### Using a new database

#### Make migrations
```
python3 manage.py makemigrations crm
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


