#imports
from tlbx_imports import *

username = ""
password = ""


#login/logout Page
@ui.page('/login')
def login():
    banner()

    #check if logged in, and display different cards based off that.
    username = app.storage.user.get('username', None)
    s = check_login()
    if s:
        is_logged_in()
    else:
        is_not_logged_in()

    footnote()





def is_logged_in():
    with ui.card():
        ui.label("You are already logged in.")
        ui.button('Log Out', on_click=try_logout)

def is_not_logged_in():
    with ui.card():
        ui.label("Log in through here!")
        username = ui.input("Username: ")
        password = ui.input("Password: ")
        ui.button('Log In', on_click=try_login)

def try_login():
    pass

def try_logout():
    pass



