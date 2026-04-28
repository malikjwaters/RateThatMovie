import csv
import psycopg2
import psycopg2.extras
from tqdm import tqdm


#Step 1, Log into the PgAdmin SQL Server
from db_info_test import *  #Info for logging into PgAdmin SQL server

conn = psycopg2.connect(
    host="dbclass.rhodescs.org",
    database="practice",
    user=DBUSER,
    password=DBPASS
)
cur = conn.cursor()

csv_path = "./csv_files/cast.csv"


#for inserting data; check if data is blank
def clean(value):
    if value is None or value == "":
        return None
    return value    # PostgreSQL will parse YYYY-MM-DD

#for closing the import
def di_closing():
    cur.close()
    conn.close()
    print("Import complete!")


#Count total num of rows
print("Counting rows...")
with open(csv_path, encoding="utf8") as f:
    total_rows = sum(1 for _ in f) - 1

print(f"Total rows: {total_rows}")
