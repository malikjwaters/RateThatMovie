#imports
from tlbx_imports import *


# Search Stuff
@ui.page('/search')
def search():
    banner()

    with ui.card():
        ui.label("Search Movies, Actors, and More!").style('font-size: 200%')

        with ui.row():
            ui.button("Movies")
            ui.button("Actors")


    footnote()