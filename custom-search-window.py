import sys, os
import tkinter as tk
from functools import partial

from tkinter import messagebox as mb
from location_reference import *
from url_builder import *
from autocomplete_entry import AutocompleteEntry

# pyinstaller --onefile --noconsole --add-data="geotargets-2019-02-11.csv;." custom-search-window.py

# Displays a pop-up error box with a custom message
def error(message):
    mb.showerror("Error", message)

def search_command(search_entry, loc_entry, searcher):
    print("searching " + search_entry.get() + loc_entry.get_str())
    loc = searcher.get_loc_by_id(searcher.get_id(loc_entry.get_str()))
    url = UrlBuilder(search_entry.get(), loc)
    print(url.url())
    webbrowser.open_new(url.url())

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


file_path = resource_path("geotargets-2019-02-11.csv")

searcher = LocationSearcher(file_path, limit=40)

window_shape = (300, 600)
query = ""

window = tk.Tk()
window.geometry(str(window_shape[0]) + 'x' + str(window_shape[1]))
window.title("International Google Search")
title1 = tk.Label(window, text="International Search", font=("", 12))
search_title = tk.Label(window, text="Enter Search Query:")
loc_title = tk.Label(window, text="Enter Location:")
search = tk.Entry(window, exportselection=0, textvariable=query)

names = [] #list(searcher.names_to_id.keys())


location_entry = AutocompleteEntry(names, searcher, window)

search_cmd = partial(search_command, search, location_entry, searcher)

button = tk.Button(window, text="Search", command=search_cmd)
# button1 = tk.Button(window, text="Get", command=location_entry.var.get())

tk.Label(window, text=query).grid(column=0, row=2)
title1.grid(column=0, row=0)
search_title.grid(column=0, row=1)
search.grid(column=1, row=1)
loc_title.grid(column=0, row=3)
location_entry.grid(column=1, row=3)
button.grid(column=0, row=5)
# button1.grid(column=1, row=3)

window.mainloop()