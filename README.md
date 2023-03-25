# EpicEvents

A CRM built on Django and Django Rest Framework

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

Install Postgress
=> link to postgress

Then open the app and create a database with theses values.

Then add the path to you systeme.
Be sur to have postgress in your path before installing psycopg2

``` 
export PATH=/Library/PostgreSQL/Version/bin:$PATH
```

### Install the requirements
``` 
pip install -r requirements.txt
```

## Database



### Using the actual database

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

## Actions and permissions

| Action | Permission |
|-|-|
| Signup | Everyone |
| Login | Everyone who had signup |
| Create a project | Every logged user |
| Add and remove contributors of a project | Project creator |
| Create issues and comments | Project contributor/creator |
| List and read issues | Project contributor/creator |
| List and read comments | Project contributor/creator |
| Modify or delete project, issue and comment | Project/Issue/Comment creator |
| All actions on all objects | Superuser |

## API documentation
On the documentation, you can see all the endpoints and also some rules about permissions, contraints and restrictions.



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

