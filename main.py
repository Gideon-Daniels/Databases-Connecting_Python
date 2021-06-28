import mysql.connector
# Connect to python
mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                               database="Hospital",
                               auth_plugin="mysql_native_password")
mycursor = mydb.cursor()
# Inserting a record into database
sql_insert = "INSERT INTO Dentists VALUES(%s, %s, %s, %s, %s)"
val = ("GDP", "Godwin", "Dr Dzvapatsva", "0735887757", "1023450")
mycursor.execute(sql_insert, val)

# Update a Record in MySQL Table
sql_update = "UPDATE Dentists SET Dentist_surname = 'Myberg' WHERE Dentist_names = Godwin"

mydb.commit()

print(mycursor.rowcount, "record inserted.")
mycursor.execute("Select * from Dentists")
for i in mycursor:
    print(i)
