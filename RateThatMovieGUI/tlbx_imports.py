#file from where common imports are put in

import psycopg
from psycopg.rows import dict_row

import nicegui
from nicegui import ui, app

# imports of other files
from db_info import *
from db_actions import *
from tlbx_webfunctions import *




# Connect to an existing database
conn = psycopg.connect(f"host=dbclass.rhodescs.org dbname=practice user={DBUSER} password={DBPASS}")

# Open a cursor to perform database operations
cur = conn.cursor(row_factory=dict_row)
