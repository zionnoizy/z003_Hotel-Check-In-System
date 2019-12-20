#!/usr/bin/python3
#!/usr/bin/python

import sys
sys.path.insert(0, "/home/pi/pi-rc522/ChipReader")
#from pirc522 import RFID
#import signal
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import json
#import iota
from datetime import datetime
#import MFRC522
from prettytable import PrettyTable
#from firebase import firebase
#fb = firebase.FirebaseApplication('https://xxxx.com/', None)
#fb.put('test/asdf',"count", 4)
#import MYSQLdb
import mysql.connector
import mysql.connector as mariadb
import os
#from twilio
from twilio.rest import Client

reader = SimpleMFRC522()

mydb = mysql.connector.connect(host='localhost', user='exampleuser', passwd='pimylifeup', database='db1') #mariadb

account_sid = "AC3ddb11e9c78366bc49e3fe95e56fc608"
auth_token = "b01ebebe3712eee84ddbdc8d669179ca"
client = Client(account_sid, auth_token)

try:
    while True:
        print ("Welcome hotal management system")
        print ("Press Ctrl-C to stop")
        room_num = raw_input("\nPlease enter room number and press enter (1/2):")
        print (room_num)

        if (room_num == '1' or room_num == '2'):
            name = raw_input("\nPlease enter name and press enter:")
            CIS = raw_input("\nSelect check-in / check-out:")
            print("Hold your ID card near the reader")
            (tagID, text) = reader.read() #scan card

            mycursor = mydb.cursor(buffered=True)
            if CIS=="check-in":
                print("Welcome to check in")
                #mycursor = mydb.cursor()
                print (tagID, room_num, name, CIS)
                sql = "INSERT INTO hotel (tagID, room_num, name, status) VALUES (%s, %s, %s, %s);" #sql table, variable
                val = (tagID, room_num, name, CIS)
                mycursor.execute(sql, val)
                mydb.commit()
                json_data_ci = {'tagID': str(tagID), 'room_number': room_num, 'Name': name, 'CIS': CIS}
                print (json_data_ci)
                print(mycursor.rowcount, "record inserted")
            elif CIS=="check-out":
                print("Thank you for check out, have a nice trip")

                mycursor.execute("SELECT tagID from hotel")
                r = mycursor.fetchone()
                print(str(r[0]), tagID)
                if str(tagID) != str(r[0]):
                    ##
                    #client.messages.create(
                    #  to="+12533533309",
                    #  from_="+12537991699",
                    #  body="Warning! Someone is trying to go in your room.",
                    #)
                    print ("Warning! not the same tag id card!")
                else:
                    val2 = str(tagID)
                    sql2 = "DELETE FROM hotel WHERE tagID =" + "'" + val2 + "'" + ";" #deletec one row

                    mycursor.execute(sql2) #, val2
                    mydb.commit()
                    print(mycursor.rowcount, "record deleted")
        else:
            print("wrong room number, start over again!")
            break;

except KeyboardInterrupt:
    print("cleaning up")
    GPIO.cleanup()