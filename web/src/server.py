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

  # Route to add guests
  config.add_route('add_guest', '/add_guest')
  config.add_view(add_guest, route_name='add_guest')

  config.add_static_view(name='/', path='./public', cache_max_age=3600)

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 6000, app)
  server.serve_forever()


