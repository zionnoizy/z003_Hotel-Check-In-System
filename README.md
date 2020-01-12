# Hotel-Check-In-System
This project is from Advance Security CINS course, using RFID MFRC-522 to build self-check in system in Raspberry Pi.
Program used: HTML, php, MySQL, Python, json
![IOT_hotel_](https://user-images.githubusercontent.com/54279382/72212479-f5fb2280-3491-11ea-886f-0421ca16fd12.png)

## Built With

* [SimpleMFRC522](https://github.com/pimylifeup/MFRC522-python) - The scranning of hotel cards
* [Twilio](https://www.twilio.com/) - Send suspicious check-in attempt
* [MariaDB](https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/) - Manage data stored in Python

## Description
After the python program runs, the users enter the hotel information (room num, name, check-in). The users require to use hotel cards to check their identity. All the information will update to the website automatically after successful check-in. To check-out, the users need to type all the information systems and use the hotel cards. The information will delete after the users select check-out.

## Explanation 
In the python program, it contains SimpleMFRC522 library to identify the RFID hardware. First, the program connects to the local database with the database username and password using MySQL connector. Inside the while loop, it asks for hotel information input. There are two main conditions (check-in/check-out). If the users are checking-in, SQL will create INSERT Query to execute and commit the existing database to the system. On the other hand, to checking-out, the users choose check-out status to delete existing data in the database. In html, we make a connection for the database and then present the most recent data using PHP. The result is shown in each row using a while loop. There is a total of one hotel card with a unique id for each user. If hackers attempt to use different hotel cards different than the users' one, the system will send a suspicious text message to your cell phone number. The python uses Twilio library to finish the text message action.
