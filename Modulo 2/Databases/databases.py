import sqlite3
import pandas as pd

# load data
df = pd.read_csv('logs.csv')
df.head()

# Clean data
df.columns = df.columns.str.strip()

# Create SQLite database
connection = sqlite3.connect('demo.db')

# Create table and Load data file to SQLite
df.to_sql('logs',connection, if_exists='replace')

# Close connection
connection.close