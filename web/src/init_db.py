# Import MySQL Connector Driver
import mysql.connector as mysql

# Load the credentials from the secured .env file
import os
from dotenv import load_dotenv
load_dotenv('credentials.env')

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST'] # must 'localhost' when running this script outside of Docker

# Connect to the database
db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = db.cursor()

# ===================================================================== Guestbook ==============
# # CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!!
cursor.execute("drop table if exists Guestbook;")

try:
  cursor.execute("""
    CREATE TABLE Guestbook (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      first_name  VARCHAR(30) NOT NULL,
      last_name   VARCHAR(30) NOT NULL,
      email       VARCHAR(50) NOT NULL,
      created_at  TIMESTAMP
    );
  """)
except:
  print("Guestbook table already exists. Not recreating it.")

# Insert Records
query = "insert into Guestbook (first_name, last_name, email, created_at) values (%s, %s, %s, %s)"
values = [
  ('rick','gessner','rick@gessner.com', '2020-02-20 12:00:00'),
  ('ramsin','khoshabeh','ramsin@khoshabeh.com', '2020-02-20 12:00:00'),
  ('al','pisano','al@pisano.com', '2020-02-20 12:00:00'),
  ('truong','nguyen','truong@nguyen.com', '2020-02-20 12:00:00')
]
cursor.executemany(query, values)
db.commit()

# Selecting Records
cursor.execute("select * from Guestbook;")
print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]

# ===================================================================== Personal ===============
# # CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!!
cursor.execute("drop table if exists Personal;")

try:
  cursor.execute("""
    CREATE TABLE Personal (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      first_name  VARCHAR(30) NOT NULL,
      last_name   VARCHAR(30) NOT NULL,
      email       VARCHAR(50) NOT NULL,
      created_at  TIMESTAMP
    );
  """)
except:
  print("Personal table already exists. Not recreating it.")

# Insert Records
query = "insert into Personal (first_name, last_name, email, created_at) values (%s, %s, %s, %s)"
values = [
  ('Chaztine','Embucado','cembucad@ucsd.edu', '2020-02-20 12:00:00'),
]
cursor.executemany(query, values)
db.commit()

# Selecting Records
cursor.execute("select * from Personal;")
print('---------- DATABASE INITIALIZED ----------')
[print(y) for y in cursor]

# ===================================================================== Education ==============
# # CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!!
cursor.execute("drop table if exists Education;")

try:
  cursor.execute("""
    CREATE TABLE Education (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      school  VARCHAR(50) NOT NULL,
      degree   VARCHAR(30) NOT NULL,
      major       VARCHAR(50) NOT NULL,
      date       VARCHAR(50) NOT NULL,
      created_at  TIMESTAMP
    );
  """)
except:
  print("Education table already exists. Not recreating it.")

# Insert Records
query = "insert into Education (school, degree, major, date) values (%s, %s, %s, %s)"
values = [
  ('Univeristy of California, San Diego','B.S.','Electrical Engineering', '2022'),
]
cursor.executemany(query, values)
db.commit()

# Selecting Records
cursor.execute("select * from Education;")
print('---------- DATABASE INITIALIZED ----------')
[print(z) for z in cursor]

# ===================================================================== Project ================
# # CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!!
cursor.execute("drop table if exists Project;")

try:
  cursor.execute("""
    CREATE TABLE Project (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      title  VARCHAR(30) NOT NULL,
      description   VARCHAR(50) NOT NULL,
      link       VARCHAR(50) NOT NULL,
      image_src       VARCHAR(50) NOT NULL,
      team       VARCHAR(50) NOT NULL,
      created_at  TIMESTAMP
    );
  """)
except:
  print("Project table already exists. Not recreating it.")

# Insert Records
query = "insert into Project (title, description, link, image_src, team) values (%s, %s, %s, %s, %s)"
values = [
  ('BallBuddy','soccer ball with data!','TBD', 'TBD', 'smartspherez'),
]
cursor.executemany(query, values)
db.commit()

# Selecting Records
cursor.execute("select * from Project;")
print('---------- DATABASE INITIALIZED ----------')
[print(p) for p in cursor]

db.close()
