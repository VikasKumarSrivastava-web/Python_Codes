import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="mypostgresdb", user='postgres', password='Vikas143*', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
#
cursor.execute("Insert into work.customer values(4,'bishal','shimla',1234567890)")
conn.commit()
cursor.execute("select * from work.customer")
# Fetch a all rows using fetchall() method.
data = cursor.fetchall()
print(data)

#Closing the connection
conn.close()
