# Testing Get Data From API

#install pyodbc

import pypyodbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = '10.32.1.51,1455'
DATABASE_NAME = 'ecis'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=True;
    uid=<'sa'>;
    pwd=<'Exim1234'>;
"""
conn = pypyodbc.connect(connection_string)
print(conn)


# test 2

import pyodbc

try:
    conn = pyodbc.connect("Driver={SQL Server};"+
                        "Server=10.32.1.51,1455;"+
                        "Database=ecis;"+
                        "Trusted_Connection=no;"+
                        "uid=sa;"+
                        "pwd=Exim1234")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usermaster')
    print('Connected')
except pyodbc.Error as ex:
    print('Failed',ex)
    
# test 3

import pyodbc
import pandas

conn=pyodbc.connect(
    Trusted_Connection = "Yes",
    Driver = {'ODBC Drivever 17 for SQL Server'},
    Server="10.32.1.51,1455",
    Database="AIMS",
    uid="sa",
    pwd="Exim1234"
)

cursor=conn.cursor()

cursor.execute("select * from audit_finding_detail;")

for row in cursor:
    print(row)

df=pandas.read_sql_suery("SELECT * FROM audit_finding_detail", conn)
df.head()

# test 4
#succeed in EXIM
#https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16
#installation

#smss
#https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16#download-ssms


#.install .cer or enable SSL

import pyodbc
import pandas as pd
 
try:

    # setup url 

    # load privatekey
    # create jwtToken 
        # header
        # payload
        # signature

    # build the url connect (url + jwtToken)

    # responseCode 
    # check if 200 
    # else throw error




    conn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};"+
                        "Server=10.32.1.51,1455;"+
                        "Database=ecis;"+
                        "Trusted_Connection=no;"+
                        "uid=sa;"+
                        "pwd=Exim1234;"+
                        "Encrypt=yes;"+
                        "TrustServerCertificate=yes;")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usermaster')
    for row in cursor:
        print('row = %r' % (row,))
   
    df=pd.read_sql_query("select * from usermaster",conn)
    print(df)
    print('Connected')
except pyodbc.Error as ex:
    print('Failed',ex)