

# main file for collecting data from sensors
from sense_hat import SenseHat
import sqlite3
import time


conn = sqlite3.connect("../database.db") #SQLite3 Setup
c = conn.cursor() #SQL Cursor

c.execute("DROP TABLE data")

c.execute("CREATE TABLE IF NOT EXISTS data (date STRING, time STRING, humidity STRING, temp STRING, pressure STRING)")

s = SenseHat() #Sensehat Setup



def get_data(): #Get humidity and temperature
    humidity = s.get_humidity()
    temp = s.get_temperature()
    pressure = s.get_pressure()
    print("""
Current Humidity: """ + str(humidity) + """
Current Temperature: """ + str(temp) + """
Current Air Pressure: """ + str(pressure))
    date = time.strftime("%Y-%m-%d", time.gmtime())
    ctime = time.strftime("%H:%M", time.gmtime())
    print("Date: " + str(date))
    print("Time: " + str(ctime))

    c.execute("INSERT INTO data (date, time, humidity, temp, pressure) VALUES(?, ?, ?, ?, ?)", [date, ctime, humidity, temp, pressure])
    conn.commit()
    


while True:
    get_data()
    time.sleep(10)

 
