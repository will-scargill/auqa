import os

# tell the program we are testing so we don't import anything
# that is just for the pi
os.environ["TEST"] = "y"

# import dashboard and sense
import dashboard.index as dashboard
import sense.index as sense

# import database
import sqlite3

# connect to database
db_conn = sqlite3.connect("database.db")
db_c = db_conn.cursor()

# make a new web server
test_app = dashboard.app.test_client()
