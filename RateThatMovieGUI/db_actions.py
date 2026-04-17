#imports
from tlbx_imports import *


def get_movies():
    cur.execute("SELECT * FROM movies;")
    movs = cur.fetchall()
    return movs

def get_genres():
    cur.execute("SELECT * FROM genres;")
    genres = cur.fetchall()
    return genres

# Account
def create_account(username, password):
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", [username, password])
    conn.commit()

def check_account(username):
    cur.execute("SELECT * FROM users WHERE username=%s", [username])
    if cur.rowcount != 0:
        return True
    else:
        return False

def get_password_for_username(username):
    cur.execute("SELECT password FROM users WHERE username=%s", [username])
    password = cur.fetchone()[0]
    return password