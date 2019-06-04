<!-- <img src="/static/images/greenesto_logo.png" height="100px" width="350px"> -->
<h3>Which technologies we are using</h3>
1. python 2.7
2. mySQL
3. Ubuntu
4. django 1.9.6
<h3> Intructions for setting up project </h3>
<ol>
  <li>
    <h4>In linux</h4>
    <ul type='disc'>
    <li>`sudo apt-get install python-pip`</li>
    <li>`sudo pip install virtualenv`</li>
    <li>`sudo apt-get install mysql-server`</li>
    <li>`sudo apt-get install python-dev`</li>
    <li>`sudo apt-get install libmysqlclient-dev`</li>
    <li>`sudo pip install MySQL-python`<li>
    -- now create a virtual environment for the project, we will name it "project" --
    <li>`virtualenv project`</li>
    -- now activate your virtual environment , we will install our dependecies in that virtual environment
    <li>`source project/bin/activate`</li>
    -- now we will install our dependecies, NOTE: dont use sudo now
    <li>`pip install django`</li>
    -- now clone our project to your working directory
    <li>`git clone https://github.com/vipin14119/greenesto.git`</li>
    -- You are done now setting up the project --
    </ul>
  </li>
  <li>
    <h4>In windows</h4>
  </li>
</ol>

<h3>Firing up the project</h3>
After installing correct dependencies you have to do few more task to running the server correctly.
<li>1. You have to create a database first to which you can connect</li>
<li>2. type `mysql -u root -p`</li>
<li>3. now create a database named `greenesto`</li>
<li>4. create database greenesto;</li>
<li>5. now exit from mysql shell</li>
<li>6. go to Greenesto/localSetting.py</li>
<li>7. change password from `09091996` to your mysql password.</li>
<li>8. now apply these changes to database.
<li>9. type `python manage.py makemigrations` followed by `python manage.py migrate`</li>
<li>10. Now you are done with settings.</li>
<li>11. type `python manage.py runserver`</li>
<li>12. You should be able to view index.html page on `127.0.0.1:8000/`</li>

<h3>Little Intro to Project</h3>
Now lets take a simple tour to our project
We divided our project into multiple parts(django apps) to make it east to contribute.
See below for descriptions of different apps
<li>1. `Greenesto` , It is our main `Django-Project`, contains settings,wsgi,urls </li>
<li>2. `main` , It is `django-app` for Main page, it has index.html, about.html, contact.html</li>
<li>3. `solar` , It is `django-app` for e-commerce part</li>
