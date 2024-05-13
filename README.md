
# Project Title

Word Search using Django


## Description
Created a REST API that takes in multiple paragraphs of text as input, stores each paragraph 
and the words to paragraph mappings on a Relational database. 

Given a word to search for, it lists out the top 10 paragraphs in which the word is present.


## Functionality
● User should first login via the api 
● All subsequent api requests must be authenticated or else they will fail 
● The API should follow typical RESTful API design patterns. 
● The data should be saved in the  DB. 

## API end points(on local HOST)
http://127.0.0.1:8000  ## Home(login page)

http://127.0.0.1:8000/register/  ## for new user registration

http://127.0.0.1:8000/paragraph/   ## To input Paragraph

http://127.0.0.1:8000/search_paragraph/  ## To search word in paragraph
## Deployment
Must install Python , Django and create virtual environment

To deploy this project run
```bash
  python manage.py makemigrations
```
```bash
  python manage.py migrate
```

```bash
  python manage.py runserver
```

