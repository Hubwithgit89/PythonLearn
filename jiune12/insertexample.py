import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='pynative',
                                         password='pynative@#29')
    cursor = connection.cursor(prepared=True)
    sql_insert_query = """ INSERT INTO `employee`
                       (`id`, `name`,`salary`,`city`) VALUES (%s,%s,%s,%s)"""
    emp_id = 3
    emp_name = "Jason"
    salary = 8000
    city = "New York"
    insert_tuple = (emp_id, emp_name, salary, city)
    result = cursor.execute(sql_insert_query, insert_tuple)
    connection.commit()
    print("variable inserted successfully into employee table using the prepared statement")
except mysql.connector.Error as error:
    connection.rollback()
    print("parameterized query failed {}".format(error))
finally:
    # closing database connection.
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
