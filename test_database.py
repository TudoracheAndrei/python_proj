import pyodbc

# Define the connection string
conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=DESKTOP-H6HQDSS;'
    r'DATABASE=Training;'
    r'Trusted_Connection=yes;'
)

# Establish a connection to the database

conn = pyodbc.connect(conn_str)

# Create a cursor from the connection

cursor = conn.cursor()

# Execute a query

try:
    # Execute a query
    cursor.execute('SELECT * FROM dbo.orase')

    # Fetch the results
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
       print(row)

except Exception as e:
   print(f"An error occurred: {e}")