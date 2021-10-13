# QuizApplication
## Quiz Application is created using Python Django, Javascript, Jquery and using mySQL database. 

### MySQL Database
  - NAME: djangoquiz
  - ENGINE: 127.0.0.1
  - POST: 3306


### Django SERVER 
   - http://127.0.0.1:8000/

## Steps to run application in Django:
- First create a database in mySQL database. 
Name of database should be `djangoquiz` .


- Then run 

`python manage.py makemigrations`

`python manage.py migrate` 

so tables will create in database .


- Now run `python manage.py runserver`

- On server's homepage it'll show `No Quiz Available !!`, that's because no data inserted in `djangoquiz` table.

- So Insert data in `djangoquiz` table like Question, Option1, Option2, Option3, Option4 and a Corrans i.e Correct Answer.

- Then on server homepage quizes will appear.

# Thank You !!


