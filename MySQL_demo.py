import mysql.connector

# get word to lookup from user
word = input("What word do you wish to define?:")
# provide user, password, host and database name
conn = mysql.connector.connect(user="ardit700_student",
                               password="ardit700_student",
                               host="108.167.140.122",
                               database="ardit700_pm1database")

cursor = conn.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression='%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result)
else:
    print("Sorry, look up word not found.")
