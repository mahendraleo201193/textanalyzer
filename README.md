# textanalyzer
This application accepts a text file as input and then analyze the text file in order to result the word count.
For Example:
  - If a text file contains : "Hello worlD Hello Hello world"
  - The output would be like this:
            world=2
            hello=3
            
## Technology used:
    - Python Django
    
## PreReqs:
    - Python2.7 and above
    - Mysql up and running with below configuration:
          'NAME': 'djangodatabase',
          'USER': 'root',
          'PASSWORD': 'password',
          'HOST': 'localhost',
          'PORT': '3306'
     - Django Installation
     
## How to start the server:
     - Navigate to the folder myproject from the terminal
     - run the command : "python manage.py runserver"
     
## How to access from the browser:

     - http://127.0.0.1:8000/myapp/home/
     - put the filename and upload the file 
     - click on the go button

