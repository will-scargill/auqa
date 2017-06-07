from nose.tools import *
import random

from tests import sense, db_conn, db_c

# Check the program can put stuff in the database.
def test_put_into_database():
    # Generate random 'ballpark' values
    humidity = random.uniform(30, 80)
    temperature = random.uniform(10, 30)
    pressure = random.uniform(1000, 2000)

    # Insert the data using the function in /sense/index.py
    # and get the returned id.
    id = sense.insert_data(humidity, temperature, pressure)

    # Use the returned id to get the inputted data
    db_c.execute("SELECT humidity, temperature, pressure FROM `data` WHERE id = ?", [id])

    data = db_c.fetchall()[0]

    # Check each value in the database is what it should be
    assert data[0] == humidity
    assert data[1] == temperature
    assert data[2] == pressure
