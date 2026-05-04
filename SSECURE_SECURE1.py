import os
from dotenv import load_dotenv

import mysql.connector as mycon
mydb = mycon.connect(host=os.getenv("DB_HOST"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"))


dbc = mydb.cursor()
dbc.execute("CREATE DATABASE SBANK")