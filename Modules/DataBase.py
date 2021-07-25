import mysql.connector
from configparser import ConfigParser
from Modules import ErrorDataBaseConnection

filename = 'config.ini'
section = 'mysql'

parser = ConfigParser()
parser.read(filename)

db = {}
items = parser.items(section)
for item in items:
    db[item[0]] = item[1]

try:
    con = mysql.connector.MySQLConnection(**db)
    cursor = con.cursor()
except:
    #print("Failed to consult record into table {}".format(error))
    ErrorDataBaseConnection.ErrorConnection()