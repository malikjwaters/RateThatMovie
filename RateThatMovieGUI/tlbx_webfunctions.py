#import everything
from tlbx_imports import *

def banner():
    #header
    with ui.header().style('background-color: #6a95d9'):
        with ui.row():
            ui.label("🎥").style('font-size: 200%')
            ui.label("RateThatMovie!").style('color: #FFFFFF; font-size: 200%; font-weight: 300')

    #left sidebar, for space
    with ui.left_drawer().style('background-color: #94acd1').props('width=50 bordered'):
        pass

    #right sidebar
    with ui.right_drawer().style('background-color: #94acd1'):
        # The Buttons
        ui.button('Home', on_click=lambda: ui.navigate.to('/'))
        ui.button('Login / Logout', on_click=lambda: ui.navigate.to('/login'))
        ui.button('Create Account', on_click=lambda: ui.navigate.to('/create_account'))


def footnote():
    ui.separator()
    ui.label("Credits go to Malik Waters, Peter Kennedy, and Joshua Hwang.")


# Return true if logged in, false if not logged in
def check_login():
    username = app.storage.user.get('username', None)  # default if not logged in is None
    if username is not None:
        return True
    else:
        return False


def check_login_msg():
    s = check_login()
    username = app.storage.user.get('username', None)  # default if not logged in is None
    if s:  # true
        ui.label("Welcome, " + username + ".")
    else:
        ui.label("You are not logged in.")

