#imports
from tlbx_imports import *
from ui_toolbox import *
from db_actions import *

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




#NOT LOGGED IN & LOGGING IN
def is_not_logged_in():
    with ui.card():
        ui.label("Log in through here!")
        username = ui.input("Username: ")
        password = ui.input("Password: ")
        ui.button('Log In', on_click=try_login)

def try_login():
    #first, check if user even exists
    user_id = get_user_id(username, password)
    #if user exists
    if user_id != None:
        #check if user's account's password matches typed password
        user_password = get_user_password(user_id)
        if user_password == password:
            app.storage.user['username'] = username
            ui.navigate.to('/') #go home

    #if user does not exist OR is wrong password...
    else:
        ui.notify('Wrong username or password', color='negative')



#LOGGING IN & LOGGING OUT (FROM BEING LOGGED IN)
def is_logged_in():
    with ui.card():
        ui.label("You are already logged in.")
        ui.button('Log Out', on_click=try_logout)

def try_logout():
    with ui.card():
        app.storage.user.pop('username')
        ui.label("You are now logged out.")
        ui.button('Back to Homepage', on_click=lambda: ui.navigate.to('/'))



