# Polling App

>This is a simple voting system implemented using django.

## Quick start guide

```
# Install dependencies
pipenv install
```
```
# Enter the virtual environment.
pipenv shell
```
```
cd polling_system
```
```
# Serve on localhost:8000
python manage.py runserver
```
```
# Create admin user
python manage.py createsuperuser
```
```
username:admin
password:admin12345
```

## Personal Conclusion

This is my first time to learn and use django, using the sqlite3 database that comes with the django framework. I implemented a simple polling system and created two tables, one for storing questions and timestamps, and one for storing options for questions.

The surprise that Django brings to me is that it comes with its own back-end admni management system. The personnel authorized by the admin can directly operate the back-end, and it also comes with sqlite3. Compared to the Flask framework I have used before, Flask does not have a specified database. You can use My SQL or No SQL. Additionally, Flask relies on various flexible extensions (such as mail Flask-Mail, user authentication Flask-Login, database Flask-SQL Alchemy) to add additional features to web applications.

Since I had a mild low temperature fever after being vaccinated Pfizer on the day of the interview, I took a rest for a couple days before starting to build the project. Therefore, I did not have enough time to write and test the login and registration function. In the follow-up, I will gradually improve this voting system in my free time and add features such as JWT Authentication.

In the process of using django, there is one thing that has always been more uncomfortable, and that is to use the template that comes with django. This way of using html+css+js on its own always feels like the practice of the previous era. The separation of front-end and back-end is good for development efficiency, multi-end support, and so on.

In previous projects, I usually used React-router-dom to control the page render in the front-end React, and Node.js was responsible for pass data stream. But django uses `urls.py` to control the rendering of the page. How to use webpack to configure front-end and back-end separation to make front-end work more free is the direction I will learn later.# Polling-App-Django-Starting-Project

I like this interview very much. The interviewer is very warm and friendly. It makes me feel that UNSW is a place where I can improve my skills.