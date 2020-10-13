import cx_Oracle

connection = None
try:
    connection = cx_Oracle.connect("hr/hr@127.0.0.1/orcl")

    cur = connection.cursor()
    cur.execute("select * from EMPLOYEES")

    for line in cur:
        print(type(line))
        print(line)

except cx_Oracle.Error as error:
    print(error)

finally:
    # release the connection
    if connection:
        connection.close()


