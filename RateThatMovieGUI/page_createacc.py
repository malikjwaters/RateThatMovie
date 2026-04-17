#import everything
from tlbx_imports import *


# Variables
username = ""
password = ""


# Create a New Account
@ui.page('/create_account')
def create_account():
    banner()

    with ui.card():
        ui.label("Create New Account!")
        username = ui.input("Username: ")
        password = ui.input("Password: ")
        ui.button('Sign Up', on_click=try_create_account)

    footnote()

def try_create_account():
    #first, check if the account even exists


    search_user = ""
    search_pswd = ""

    pass

