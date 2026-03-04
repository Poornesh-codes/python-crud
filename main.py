import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

def getConnection():
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=5433)
        return connection
    except Exception as e:
        print("Error connecting database",e)
        return None
    
def insert():
    connection=getConnection()
    """if connection is none(that is error in connecting)then insert() returns none,"""
    if connection is None:
        return
    try:
        cursor=connection.cursor()
        name = input("enter name:")
        id = (input("enter id:"))
        age = (input("enter age:"))
        query="INSERT INTO employee(name,id,age) VALUES(%s,%s,%s);"
        cursor.execute(query,(name,id,age))
        connection.commit()
        print("data inserted successfully")
    except Exception as e:
        print("error inserting data",e)
    finally:
        #either case if inserting is done or not, connection must be closed
        connection.close()

def getAll():
    connection=getConnection()
    if connection is None:
        return
    try:
        cursor=connection.cursor()
        cursor.execute('''SELECT * from employee;''')
        """
        record is list of data
        hence using for loop to print individual 
        data separately instead of list 
        """
        record = cursor.fetchall()
        for employ in record:
            print(employ)
        print("data extracted")
    except Exception as e:
        print("error retrieving data",e)
    finally:
        connection.close()


insert()
getAll()