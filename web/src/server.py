from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from pyramid.response import Response

#import pyramid.httpexceptions as exc
import mysql.connector as mysql
import os
#import requests
import json

GUEST_DB_FILE_PATH = './guest_database.txt'    # Location of guest DB relative to server.py

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']

personalK = ('first_name', 'last_name', 'email')
educationK = ('school', 'degree', 'major', 'date')
projectK = ('title', 'description', 'link', 'img_src')

def get_home(req):
  # Connect to the database and retrieve the guestbook
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email from Guestbook;")
  records = cursor.fetchall()
  db.close()
  return render_to_response('templates/home.html', {'guestbook': records}, request=req)

def welcome(req):
  # Connect to the database and retrieve the guestbook
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email from Guestbook;")
  records = cursor.fetchall()
  db.close()
  return render_to_response('templates/welcome.html', {'guestbook': records}, request=req)

def about(req):
  return render_to_response('templates/aboutus.html', {}, request=req)

def cv(req):
  return render_to_response('templates/cv.html', {}, request=req)

def add_guest(req):
  new_guest = req.json_body
  print(new_guest)
  j = json.loads(new_guest)
  newFirstName = j["first_name"]
  newLastName = j["last_name"]
  newEmail = j["email"]
  newComment=j["comment"]
  #newTime=j["created_at"]
  print(newFirstName)
  print(newLastName)
  print(newEmail)
  print(newComment)
  #print(newTime)

  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  query = "INSERT INTO Guestbook (first_name, last_name, email, comment) VALUES (%s, %s, %s, %s)"
  values = [newFirstName, newLastName, newEmail, newComment]
  cursor.execute(query, values)
  db.commit()
  db.close()

  return render_to_response('templates/home.html', {}, request=req)

def show_guests(req):
  db = mysql.connect(host = db_host, database = db_name, user = db_user, password=db_pass)
  cursor = db.cursor()
  cursor.execute("SELECT * FROM Guestbook ORDER BY ID ;" )
  guestBook = {}
  response = cursor.fetchall()
   
  guestBook['first_name'] = response[1]
  guestBook['last_name'] = response[2]
  guestBook['email'] = response[3]
  guestBook['comment'] = response[4]
  
  db.commit()
  response = Response(body=json.dumps(guestBook))
  response.headers.update({'Access-Control-Allow-Origin': '*',})

  return response

def avatar(req):
  return {"image_src": "/pics/mclarengulf.jpg"} 

def resume(req):
  return render_to_response('templates/resume.html', {}, request=req)

def personal(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email from Personal;")
  records = cursor.fetchall()
  db.close()
  return render_to_response('templates/personal.html', {'personal': records}, request=req)

def education(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select school, degree, major, date from Education;")
  records = cursor.fetchall()
  db.close()
  return render_to_response('templates/education.html', {'education': records}, request=req)

def project(req):
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select title, description, link, image_src, team from Project;")
  records = cursor.fetchall()
  db.close()
  return render_to_response('templates/project.html', {'project': records}, request=req)

def some_route_returning_json():
  # other stuff happening in your route
  SOME_DATA_ARRAY = ("help")

  # form a Response object and update the heder to allow cross-site access
  response = Response(body=json.dumps(SOME_DATA_ARRAY))
  response.headers.update({'Access-Control-Allow-Origin': '*',})
  return response

''' Route Configurations '''
if __name__ == '__main__':
  config = Configurator()

  config.include('pyramid_jinja2')
  config.add_jinja2_renderer('.html')

  config.add_route('get_home', '/')
  config.add_view(get_home, route_name='get_home')

  # route for cv
  config.add_route('cv', '/cv')
  config.add_view(cv, route_name='cv')

  # route for welcome
  config.add_route('welcome', '/welcome')
  config.add_view(welcome, route_name='welcome')

  # route for about
  config.add_route('about', '/about')
  config.add_view(about, route_name='about')

  # route to add guests
  config.add_route('add_guest', '/add_guest')
  config.add_view(add_guest, route_name='add_guest')

  # route to show guests
  config.add_route('show_guests', '/show_guests')
  config.add_view(show_guests, route_name='show_guests')

  # route to get avatar
  config.add_route('avatar', '/avatar')
  config.add_view(avatar, route_name='avatar', request_method='GET', renderer='json')

  # route to get personal
  config.add_route('personal', '/personal')
  config.add_view(personal, route_name='personal', renderer='json') 

  # route to get education
  config.add_route('education', '/education')
  config.add_view(education, route_name='education', renderer='json')

  # route to get resume
  config.add_route('resume', '/resume')
  config.add_view(resume, route_name='resume', renderer='resume')

  # route to get project
  config.add_route('project', '/project')
  config.add_view(project, route_name='project', renderer='json')  

  config.add_static_view(name='/', path='./public', cache_max_age=3600)

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 6000, app)
  server.serve_forever()


