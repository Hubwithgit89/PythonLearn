import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='pynative',
                                         password='pynative@#29')
    cursor = connection.cursor(prepared=True)
    # Delete record now
    sql_Delete_query = """Delete from employee where id = %s"""
    emp_id = 3
    
    cursor.execute(sql_Delete_query, (emp_id,))
    connection.commit()
    print("\n Record Deleted successfully ")
except mysql.connector.Error as error:
    connection.rollback()
    print("parameterized query failed {}".format(error))
finally:
    # closing database connection.
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
