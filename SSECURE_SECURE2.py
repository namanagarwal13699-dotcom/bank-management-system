import os
from dotenv import load_dotenv

import mysql.connector as mycon
mydb = mycon.connect(host=os.getenv("DB_HOST"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD") , database=os.getenv("DB_NAME"))
dbc = mydb.cursor()
#cursor.execute("create table customers(customer_id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100) NOT NULL, age INT, city VARCHAR(100))") # tables created only once
#cursor.execute("create table accounts(account_number INT PRIMARY KEY AUTO_INCREMENT, customer_id INT, account_type ENUM('saving', 'current'), balance DECIMAL(10,2), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (customer_id) REFERENCES customers(customer_id))")
#cursor.execute("create table transaction(transaction_id INT PRIMARY KEY AUTO_INCREMENT, account_number INT, type ENUM('deposit', 'withdraw', 'transfer'), amount DECIMAL(10,2), date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (account_number) REFERENCES accounts(account_number) )")
#cursor.execute("create table transfers(transfer_id INT PRIMARY KEY AUTO_INCREMENT, from_account INT, to_account INT, amount DECIMAL(10,2), date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (from_account) REFERENCES accounts(account_number))")
