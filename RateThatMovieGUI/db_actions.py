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



# Accounts / Users
def create_user(username, password):
    #Generate user_id, keep doing until unique one found...
    unique_id_found = False
    user_id = 0
    while(not unique_id_found):
        user_id = random.randint(1, 1000000)
        cur.execute("SELECT * FROM users WHERE user_id=%d", [user_id])

        if cur.rowcount == 0:
            unique_id_found = True
        else:
            unique_id_found = False

    #insert
    cur.execute("INSERT INTO users (user_id, username, password) VALUES (%d, %s, %s);", [user_id, username, password])
    conn.commit()

def check_user_exists(user_id):
    cur.execute("SELECT * FROM users WHERE username=%s", [user_id])
    if cur.rowcount != 0:
        return True
    else:
        return False

def get_user_password(user_id):
    cur.execute("SELECT password FROM users WHERE user_id=%s", [user_id])
    password = cur.fetchone()[0]
    return password

#get user_id from username and password
def get_user_id(username, password):
    cur.execute("SELECT user_id FROM users WHERE username=%s AND password=%s", [username, password])

    if cur.rowcount != 0:
        return int(cur.fetchone()[0])
    else:
        return None