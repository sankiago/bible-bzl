import sqlite3
import traceback
import sys

def connect_with_db(name):
  try:
    connection = sqlite3.connect(name)
    return connection
  except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
