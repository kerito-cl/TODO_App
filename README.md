# To-Do Django App
App used to maintain our day-to-day tasks or list everything that we have to do.

## Installation

First clone the repository:
```bash
$ git clone https://github.com/kerito-cl/TODO_App
```
Create a virtual environment to install dependencies in and activate it:
```bash
$ virtualenv env
$ source env/bin/activate
```
Install the dependencies:
```bash
(env)$ pip3 install -r requirements.txt
```

Once it has finished downloading the dependencies run the following command:
```bash
$ python3 manage.py runserver
```
![App Screenshot](https://i.ibb.co/Wt65NWb/runserver.png)

Navigate to http://127.0.0.1:8000/ in the browser


## Postgres DB Setup

Since the DB is setup in railway.app Postgres, you are ready to use the app. 
But if you want the app being setup in your local Postgres DB, you have to do the following:
```bash
$ cd todoapp
```
In settings.py :

![App Screenshot](https://i.ibb.co/MBCsBr1/setupdb.png)

Fill the corresponding details for "NAME" , "USER", "PASSWORD", "HOST" and "PORT".


## If you don't have Postgres installed 
