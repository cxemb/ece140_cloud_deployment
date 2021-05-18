from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from pyramid.response import Response

#import pyramid.httpexceptions as exc
import mysql.connector as mysql
import os
#import requests
#import json

GUEST_DB_FILE_PATH = './guest_database.txt'    # Location of guest DB relative to server.py

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']

def get_home(req):
  # Connect to the database and retrieve the guests
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/home.html', {'guests': records}, request=req)

#pages = ["cv"]

def get_cv(req):
  #pg_id = int(req.matchdict['pages'])
  #data = {'pages':pages[pg_id]}
  return render_to_response('templates/cv.html', {}, request=req)

def add_guest(req):
  new_guest = req.json_body

  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  query = "INSERT INTO guestbook (first_name, last_name, email, comment) VALUES (%s, %s, %s)"
  values = [new_guest['first_name'], new_guest['last_name'], new_guest['email'], new_guest['comment']]

  cursor.execute(query, values)
  db.commit()
  db.close()

  return render_to_response('templates/home.html', {}, request=req)

def get_avatar(req):
    return{"image_src": "143.198.59.27C:pics\mclaren-mcl35m-with-gulf-liver.jpg"}

#def get_personal(req):
#    db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
#    cursor = db.cursor()
#    cursor.execute("select first_name, last_name, email from personal;")
#    records = cursor.fetchone()
#    db.close()

#def get_education(req):
#    db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
#    cursor = db.cursor()
#    cursor.execute("select school, degree, major, date from education;")
#    records = cursor.fetchone()
#    db.close()

#def get_project(req):
#    db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
#    cursor = db.cursor()
#    cursor.execute("select title, description, link, image_src, team from project;")
#    records = cursor.fetchone()
#    db.close()

''' Route Configurations '''
if __name__ == '__main__':
  config = Configurator()

  config.include('pyramid_jinja2')
  config.add_jinja2_renderer('.html')

  config.add_route('get_home', '/')
  config.add_view(get_home, route_name='get_home')

  # route for cv
  config.add_route('get_cv', '/get_cv')
  config.add_view(get_cv, route_name='get_cv')

  # route to add guests
  config.add_route('add_guest', '/add_guest')
  config.add_view(add_guest, route_name='add_guest')

  # route to get guests
  #config.add_route('get_guest', '/get_guest')
  #config.add_view(get_guest, route_name='get_guest')

  # route to get avatar
  config.add_route('get_avatar', '/get_avatar')
  config.add_view(get_avatar, route_name='get_avatar', renderer='json')

  # route to get personal
  #config.add_route('get_personal', '/get_personal')
  #config.add_view(get_personal, route_name='get_personal', renderer='json') 

  # route to get education
  #config.add_route('get_education', '/get_education')
  #config.add_view(get_education, route_name='get_education', renderer='json')

  # route to get project
  #config.add_route('get_project', '/get_project')
  #config.add_view(get_project, route_name='get_project', renderer='json')  

  config.add_static_view(name='/', path='./public', cache_max_age=3600)

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 6000, app)
  server.serve_forever()


