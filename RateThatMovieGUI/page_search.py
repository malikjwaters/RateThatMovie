#imports
from tlbx_imports import *
from ui_toolbox import *


#non-local
search_table = None     #this will use comments

# Search Stuff
@ui.page('/search')
def search():
    uit_banner()

    #add sm code here
    with ui.card():
        ui.label("Search Movies, Actors, and More!").style('font-size: 200%')

        with ui.row():
            ui.button("Movies")
            ui.button("Actors")

    uit_footnote()

#set table up to search for movies
def set_table_movies():
    cols = [{'name': 'movie_title', 'label': 'Movie Title', 'field': 'movie_title'},
            {'name': 'movie_release_date', 'label': 'Release Date', 'field': 'movie_release_date'}]

