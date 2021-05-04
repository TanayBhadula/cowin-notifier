import requests
import json
import smtplib, ssl
import pandas as pd
from time import time, sleep
from datetime import date

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "axelrod3301@gmail.com"
receiver_email = "tanaybhadula2002@gmail.com"
password = 'ucazorkmfoztuppz'
message = """\
Subject: -- SLOT AVAILABLE --

DO REGISTRATION ASAP !!."""
context = ssl.create_default_context()

print("running......")    
while True:
    today = date.today()
    d1 = today.strftime("%d-%m-%Y")
    
    parameters = {
        "pincode": 273002,
        "date": d1
    }
    response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin', params=parameters).text
    response_info = json.loads(response)
    center_num= len(response_info['centers'])
    for i in range(center_num):
        if response_info['centers'][i]['center_id'] == 692603:
            print(response_info['centers'][i]['center_id'])
            print(response_info['centers'][i]['name'])
            session_num= len(response_info['centers'][i]['sessions'])
            
            for j in range(session_num):
                print(response_info['centers'][i]['sessions'][j]['date'])
                print(response_info['centers'][i]['sessions'][j]['min_age_limit'])
                print(response_info['centers'][i]['sessions'][j]['available_capacity'])
                print(response_info['centers'][i]['sessions'][j]['vaccine'])
                print(" ")
                
                if response_info['centers'][i]['sessions'][j]['available_capacity'] >=2:
                    print("------------- SLOT AVAILABLE REGISTER ASAP !!! ---------------")
                    try:
                        server = smtplib.SMTP(smtp_server,port)
                        server.ehlo() # Can be omitted
                        server.starttls(context=context) # Secure the connection
                        server.ehlo() # Can be omitted
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message)
                    except Exception as e:
                        # Print any error messages to stdout
                        print(e)
                    finally:
                        server.quit()
    sleep(60 - time() % 30) 
                