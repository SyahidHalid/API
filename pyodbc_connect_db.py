# !pip install pyodbc --trusted-host pypi.org --trusted-host files.pythonhosted.org

    # setup url 

    # load privatekey
    # create jwtTwoken 
        # header
        # payload
        # signature
    # build the url connect (url + jwtTowken)

    # responseCode 
    # check if 200 
    # else throw error

import pyodbc
import pandas as pd
 
try:
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
    #print(df)
    print('Connected')
except pyodbc.Error as ex:
    print('Failed',ex)


df

