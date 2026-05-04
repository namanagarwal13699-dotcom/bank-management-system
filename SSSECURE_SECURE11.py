import mysql.connector as mycon
import pyttsx3 #for speak
import time
import smtplib # foe email
import random as rn
import sys
import os
from dotenv import load_dotenv

load_dotenv() #“Read the .env file and load all values into my program”

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 140)
    engine.say(text)
    engine.runAndWait()



mydb = mycon.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

dbc = mydb.cursor()
print("\n                              ===== ╔═════════════════════════╗║ ＷＥＬＣＯＭＥ ＴＯ ＳＳＥＣＵＲＥ ＢＡＮＫ ║╚═════════════════════════╝ =====\n")

speak("welcome to s secure bank.")

print("                                                     𝒥𝓂𝓅 :- 𝒀𝒐𝒖 𝒄𝒂𝒏 𝑺𝒆𝒍𝒆𝒄𝒕 𝒀𝒐𝒖𝒓 𝑶𝒑𝒕𝒊𝒐𝒏 𝑩𝒚 𝑺𝒆𝒍𝒆𝒄𝒕𝒊𝒏𝒈 𝑰𝒕𝒔 𝑵𝒖𝒎𝒃𝒆𝒓\n")



a1 = int(input("1. Create An Account \n2. Log In \n-> "))



def account_creation(named , aged , cityd , mobile ,aty , bal , pase , email ):
     dbc.execute("insert into customers(name,age,city,mobile_no , email) values(%s,%s,%s,%s,%s)",(named ,aged ,cityd , mobile , email))
     mydb.commit()
     dbc.execute("SELECT * FROM customers ORDER BY customer_id DESC LIMIT 1")
     result = dbc.fetchone()
     cust = result[0]
     dbc.execute("insert into accounts(customer_id , account_type , balance ,password) values(%s,%s,%s,%s)",(cust ,aty , bal , pase))
     mydb.commit()
     print(f"Welcome To Ssecure Family \nYour Account Is Successfully Created \nYour Coustumer ID is: {cust}")
     speak("Your Account Is Successfully Created")




def transaction(acc , ty , amo):
     dbc.execute("insert into transaction(account_number , type , amount) values(%s,%s,%s)",(acc , ty , amo))
     mydb.commit()
     if ty == "deposit":
          dbc.execute("update accounts set balance = balance + %s where account_number = %s",(amo , acc))
          mydb.commit()

     elif ty == "withdraw":
          dbc.execute("update accounts set balance = balance - %s where account_number = %s", (amo, acc))
          mydb.commit()

     elif ty == "transfer" :
          dbc.execute("update accounts set balance = balance - %s where account_number = %s", (amo, acc))
          mydb.commit()
k = 0
while k == 0:
 if a1 == 1:

     name = input("Enter Your Name : ")
     age = input("Enter Your age : ")
     city = input("Enter Your city : ")
     mob = int(input("Enter Your mobile number : "))
     email = input("Enter Your Email : ")
     print("Please Select Your Account Type")
     ty = int(input("1. for Saving Account \n2. for Current Account \n-> "))
     acType = any
     if ty == 1:
          acType = "saving"
     elif ty == 2:
          acType = "current"
     else:
          print("invalid option")
          speak("invalid option")

     ba = 0
     pas = input("Enter Your Password (compulsory): ")
     account_creation(name ,age ,city ,mob ,acType , ba , pas , email)

     t = int(input("1. Log In \n2. Exit \n-> "))
     if t == 1:
          a1 = 2
     elif t == 2:
          sys.exit(0)
     else:
          Print("Invalid Input")
          sys.exit(0)

 if a1 == 2:
     id = int(input("Enter Your Customer Id : "))
     password = input("Enter Your Password : ")
     dbc.execute("SELECT * FROM accounts where customer_id = %s and password = %s",(id , password))
     result = dbc.fetchone()





     if result:


          acc = result[0]
          ab = 0

          while ab == 0:
            sender_email = "ssecurebank@gmail.com"
            dbc.execute("SELECT * FROM customers where customer_id = %s", (id,))
            result = dbc.fetchone()
            # receiver_email = emai
            emai = result[5]
            password = os.getenv("pass")
            x = rn.randint(111111, 999999)

            if not emai:
                 print(f"Your OTP IS: {x}")
            else:
                 message = (f"Hi \nYour OPT For LOgin In Ssecure Bank Is :{x}")
                 server = smtplib.SMTP("smtp.gmail.com", 587)
                 server.starttls()
                 server.login(sender_email, password)
                 server.sendmail(sender_email, emai, message)
                 server.quit()

                 print("OTP IS Succesfully Sended To Your Email")
                 speak("OTP IS Succesfully Sended To Your Email")



            speak("Please Enter Your 6 digit Otp")
            time.sleep(0.2)
            y = int(input("Enter Your 6 Digit OTP : "))



            if x == y :
                 ab = 1
            else:
                 print("Invalid OTP")
                 speak("Invalid OTP")

                 n = int(input("1. Resend Otp \n2. Exit \n-> "))
                 if n ==1:
                      ab == 0
                 elif n == 2:
                      sys.exit(0)
                 else:
                      print("Invalid Input")

          print("\n                               ╔═════════════════════════╗║   LOGIN SUCCESSFUL!  ║║  WELCOME BACK TO SSECURE BANK   ║╚═════════════════════════╝\n")

          speak("Login Successfully , WELCOME BACK TO S SECURE BANK")
          #time.sleep(0.4)


          a = 0
          while a == 0:

               print("1. View Account Details \n2. Deposite Money \n3. Withdraw Money \n4. Check Balance \n5. Fund Transfer \n6. Account Statement \n7. Update Bank Details \n8. Delete Bank Account \n9. Log Out \n10. Exit \n ")
               speak("Please select your next step by choosing given reference number")
               time.sleep(0.2)
               inpu = int(input())

          #inpu = int(input("1. View Account Details \n2. Deposite Money \n3. Withdraw Money \n4. Check Balance \n5. Fund Transfer \n6. Account Statement \n7. Update Bank Details \n8. Delete Bank Account \n"))


               if inpu == 1:
                    speak("Your Account Details are Given Below")
                    columns = [col[0] for col in dbc.description]
                    data = dict(zip(columns, result))
                    for key, value in data.items():
                         print(key, ":", value)

                    ex = int(input("1. Back \n2. Log out\n3. Exit \n-> "))
                    if ex == 1:
                         a = 0
                    elif ex == 2:
                         a = 1
                    elif ex == 3:
                         sys.exit(0)
                    else:
                         print("invalid option")
                         speak(f"You Select the Invalid Option")


               elif inpu == 2:
                    speak("Enter Your Amount for Deposite Money")
                    time.sleep(0.2)


                    mon = int(input("Enter Your Amount for Deposite Money : "))

                    transaction(acc ,"deposit" , mon )


                    print(f"Your Amount Of {mon} Is Succesfully Deposited")
                    speak(f"Your Amount Of Rupees {mon} Is Succesfully Deposited")

                    ex = int(input("1. Back \n2. Log out\n3. Exit \n-> "))
                    if ex == 1:
                         a = 0
                    elif ex == 2:
                         a = 1
                    elif ex == 3:
                         sys.exit(0)
                    else:
                         print("invalid option")
                         speak(f"You Select the Invalid Option")

               elif inpu == 3:
                    dbc.execute("SELECT * FROM accounts where account_number = %s", (acc,))
                    result = dbc.fetchone()
                    bal = result[3]

                    speak("Enter Your Amount for Withdraw Money")
                    time.sleep(0.2)

                    mone = int(input("Enter Your Amount for Withdraw Money : "))

                    if bal >= mone:
                          transaction(acc ,"withdraw" , mone)
                          print(f"Your Amount Of {mone} Is Succesfully Withdraded")
                          speak(f"Your Amount Of Rupees {mone} Is Succesfully Withdraded")
                    else:
                         print("⚠️ Insufficient balance")
                         speak(f"Insufficient balance")

                    ex = int(input("1. Back \n2. Log out\n3. Exit \n-> "))
                    if ex == 1:
                         a = 0
                    elif ex == 2:
                         a = 1
                    elif ex == 3:
                         sys.exit(0)
                    else:
                         print("⚠️ invalid option")
                         speak(f"You Select the Invalid Option")

               elif inpu == 4:
                    dbc.execute("SELECT * FROM accounts where account_number = %s", (acc,))
                    result = dbc.fetchone()
                    bal = result[3]
                    print(f"The available Balance In Your Account Is ₹{bal}")
                    speak(f"The available Balance In Your Account Is rupees {bal}")

                    ex = int(input("1. Back \n2. Log out\n3. Exit \n-> "))
                    if ex == 1:
                         a = 0
                    elif ex == 2:
                         a = 1
                    elif ex == 3:
                         sys.exit(0)
                    else:
                         print("⚠️ invalid option")
                         speak(f"You Select the Invalid Option")

               elif inpu == 5:
                    dbc.execute("SELECT * FROM accounts where account_number = %s", (acc,))
                    result = dbc.fetchone()
                    bale = result[3]
                    speak(f"Enter The Amount")
                    time.sleep(0.2)

                    ft = int(input("Enter The Amount: "))

                    speak(f"Enter The Receiver Account Id")
                    time.sleep(0.2)
                    tid = int(input("Enter The Receiver Account Id : "))

                    dbc.execute("SELECT * FROM accounts where account_number = %s", (tid,))
                    result = dbc.fetchone()

                    if result:

                       if bale >= ft:
                         transaction(acc, "transfer", ft)
                         dbc.execute("insert into transfers(from_account , to_account , amount) values(%s,%s,%s)",
                                     (acc, tid, ft))
                         mydb.commit()

                         dbc.execute("update accounts set balance = balance + %s where account_number = %s", (ft, tid))
                         mydb.commit()

                         print(f"Your Amount Of {ft} Is Succesfully Transferred to {tid}")
                         speak(f"Your Amount Of {ft} Is Succesfully Transferred to Account Id {tid}")
                       else:
                         print("⚠️ Insufficient balance")
                         speak(f"Insufficient balance")

                    else:
                         print("⚠️ Receiver Account Id does not exist")
                         speak(f"Receiver Account Id {tid} does not exist")

                    ex = int(input("1. Back \n2. Log out\n3. Exit \n-> "))
                    if ex == 1:
                         a = 0
                    elif ex == 2:
                         a = 1
                    elif ex == 3:
                         sys.exit(0)
                    else:
                         print("⚠️ invalid option")
                         speak(f"You Select the Invalid Option")


               elif inpu == 6:

                    dbc.execute("SELECT * FROM transaction where account_number = %s", (acc,))
                    result = dbc.fetchall()
                    print("transaction_id | account_number | type     | amount   | date")
                    for i in result:
                         print(i)

                    ex = int(input("1. Back \n2. Log out\n3. Exit \n-> "))
                    if ex == 1:
                         a = 0
                    elif ex == 2:
                         a = 1
                    elif ex == 3:
                         sys.exit(0)
                    else:
                         print("⚠️ invalid option")
                         speak(f"You Select the Invalid Option")

               elif inpu == 7:

                  speak("Please select your next operation by choosing given reference number")
                  time.sleep(0.2)

                  b = 0
                  while b == 0:

                    ch = int(input("1. Update Password \n2. Update Name \n3. Update age \n4. Update City \n5. Update Mobile Number \n6. Update Email \n7. Back \n8. Log out \n9. Exit \n-> "))
                    if ch == 1:
                         np = input("Enter Your New Password : ")
                         dbc.execute("update accounts set password = %s where account_number = %s", (np , acc))
                         mydb.commit()
                         print(f"Your New Password Is Succesfully Updated")
                         speak("Your New Password Is Succesfully Updated")

                         b = 0

                    elif ch == 2:
                         nn = input("Enter Your New Name : ")
                         dbc.execute("update customers set name = %s where customer_id = %s", (nn, id))
                         mydb.commit()
                         print(f"Your New Name Is Succesfully Updated")
                         speak("Your New Naman Is Succesfully Updated")

                         b = 0

                    elif ch == 3:
                         na = int(input("Enter Your New Age : "))
                         dbc.execute("update customers set age = %s where customer_id = %s", (na, id))
                         mydb.commit()
                         print(f"Your New Age Is Succesfully Updated")
                         speak("Your New Age Is Succesfully Updated")

                         b = 0

                    elif ch == 4:
                         nc = input("Enter Your New City : ")
                         dbc.execute("update customers set city = %s where customer_id = %s", (nc, id))
                         mydb.commit()
                         print(f"Your New City Is Succesfully Updated")
                         speak("Your New City Is Succesfully Updated")

                         b = 0

                    elif ch == 5:
                         nm = int(input("Enter Your New Mobile Number : "))
                         dbc.execute("update customers set mobile_no = %s where customer_id = %s", (nm, id))
                         mydb.commit()
                         print(f"Your New Mobile no. Is Succesfully Updated")
                         speak("Your New Mobile Number Is Succesfully Updated")


                         b = 0

                    elif ch == 6:
                         em = int(input("Enter Your New Email : "))
                         dbc.execute("update customers set email = %s where customer_id = %s", (em, id))
                         mydb.commit()
                         print(f"Your New Email Is Succesfully Updated")
                         speak("Your New Email Is Succesfully Updated")


                         b = 0




                    elif ch == 7:
                         a = 0
                         b = 1

                    elif ch == 8:
                         a = 1
                         b = 1

                    elif ch == 9:
                         sys.exit(0)

                    else:
                         print("⚠️ invalid option")
                         speak("invalid option")

               elif inpu == 8:
                    reason = input("Enter Your Reason : ")
                    dbc.execute("DELETE FROM accounts WHERE  account_number = %s", (acc,))
                    mydb.commit()
                    dbc.execute("DELETE FROM customers WHERE  customer_id = %s", (id,))
                    mydb.commit()
                    print(f"Your Account Is Succesfully Deleted")
                    speak(f"Your Account Is Succesfully Deleted")

                    ex = int(input("1. Back \n2. Log out\n3. Exit \n-> "))
                    if ex == 1:
                         a = 0
                    elif ex == 2:
                         a = 1
                    elif ex == 3:
                         sys.exit(0)
                    else:
                         print("⚠️ invalid option")
                         speak(f"You Select the Invalid Option")

               if inpu == 9:
                    a = 1
                    print("Log Out Successfully")
                    speak(f"Log Out Successfully")

               elif inpu == 10:
                    sys.exit()





     else :
          print("❌ Invalid ID or Password")
          speak("Invalid ID or Password")
          sys.exit(0)


 else:
      print("⚠️ invalid Input")
      speak("Invalid Input")
      sys.exit(0)
