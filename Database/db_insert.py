#Loading Packages
import pymysql

#Load credentials
#You could always change these from input, I just wanted to test and see if it worked before I posted this
dbhost = input() #Enter the AWS RDS address here (didn't want to hard code it in becase of security and positng this on github)
dbuser = input() #Enter the username
dbpw = input() #Enter the password

#Choosing the schema within the database
dbschema = "step_up"

#Connecting to the MySQL Database
dbconn = pymysql.connect(host = dbhost, user = dbuser, passwd = dbpw, db = dbschema,
                         use_unicode = True, charset = "utf8mb4", autocommit = True)
cursor = dbconn.cursor()
print("Connected to MySQL")


#Read in the data
import pandas as pd
import numpy as np
df = pd.read_excel("C:\\Users\\Owner\\Documents\\COA\\Throw Away\\All Donations All-Time-2023-09-13-14-58-35.xlsx",
                   header = 10,
                   index_col = [0, 2])
                   #index_col = [1, 3, 4, 5, 6, 7])
df = df[:-5]
df = df.replace({np.nan:None})
df['Close Date'] = pd.to_datetime(df["Close Date"], infer_datetime_format = True)

#Setup Query
query = "INSERT INTO TRANSACTIONS\
        VALUES(%s, %s, %s, %s, %s, %s, %s)"

#Heres the query
for i in range(len(df)):
    cursor.execute(query, (None,
                           df.iloc[i, 0],
                           df.iloc[i, 1],
                           df.iloc[i, 2],
                           df.iloc[i, 3],
                           df.iloc[i, 4],
                           df.iloc[i, 5]))
print("Executed Query")


#Always Remember to close the connection
dbconn.close()
print("Connection Closed")