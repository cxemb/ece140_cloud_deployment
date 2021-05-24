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

# # CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!!
#cursor.execute("drop table if exists Guestbook;")

# Create a TStudents table (wrapping it in a try-except is good practice)
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

# # CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!!
#cursor.execute("drop table if exists Personal;")

# Create a TStudents table (wrapping it in a try-except is good practice)
try:
  cursor.execute("""
    CREATE TABLE Personal (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      first_name  VARCHAR(30) NOT NULL,
      last_name   VARCHAR(30) NOT NULL,
      email       VARCHAR(50) NOT NULL,
      created_at  TIMESTAMP

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

db.close()
