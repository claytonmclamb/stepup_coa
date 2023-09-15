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

#Heres the query
query = "SELECT * FROM TRANSACTIONS"
cursor.execute(query)
result = cursor.fetchall()
print("Executed Query")

print(result)


#Always Remember to close the connection
dbconn.close()
print("Connection Closed")