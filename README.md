# 💡QuizApplication
## Quiz Application is created using Python-Django, Javascript, Jquery and using mySQL database. 

## 🔨Steps to run application in Django:
- First create a database in mySQL database `CREATE DATABASE djangoquiz` 

- Open terminal where `manage.py` file is located and run these commands in terminal

  `python manage.py makemigrations`

  `python manage.py migrate` 

  this will create tables in the database .


- Now run `python manage.py runserver`

- On server's homepage it'll show `No Quiz Available !!`, that's because no data inserted in `djangoquiz` table.

- So Insert data in `djangoquiz` table like Question, Option1, Option2, Option3, Option4 and a Corrans i.e Correct Answer.
- To insert data consider following mySQL query ` INSERT INTO 'quiz_exam'('id', 'Question', 'Option1', 'Option2', 'Option3', 'Option4', 'Answer') VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]','[value-7]') `

- Then on server homepage questions with their options will appear.

# 📚Happy Learning
