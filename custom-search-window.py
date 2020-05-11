import sys, os
import tkinter as tk
from functools import partial

from tkinter import messagebox as mb
from location_reference import *
from url_builder import *
from autocomplete_entry import AutocompleteEntry

import subprocess

# pyinstaller --onefile --noconsole --add-data="geotargets-2019-02-11.csv;." custom-search-window.py

# Displays a pop-up error box with a custom message
def error(message):
    mb.showerror("Error", message)

def search_command(search_entry, loc_entry, searcher):
    print("searching " + search_entry.get() + loc_entry.get_str())
    loc = searcher.get_loc_by_id(searcher.get_id(loc_entry.get_str()))
    url = UrlBuilder(search_entry.get(), loc)
    print(url.url())
    # webbrowser.open_new(url.url())
    subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "-incognito", url.url()])

def open_translate_command():
    print("Opening Translate")
    subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "-incognito", r'https://translate.google.com/?sl=auto&tl=en'])
    # webbrowser.open_new(r'https://translate.google.com/?sl=auto&tl=en')

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


file_path = resource_path("geotargets-2019-02-11.csv")
window_shape = (400, 400)
searcher = LocationSearcher(file_path, limit=40)

instructions_str = """
TO SEARCH LOCAL ENGLISH SOURCES FROM TARGET LOCATION:
1. Select target country
2. Type search query in English
3. Click "Search"


TO SEARCH LOCAL LANGUAGE SOURCES FROM TARGET LOCATION (RECOMMENDED):
1. Select target country
2. Click "Open Translate" to open up a google translate window
3. Translate your search query into a native language of the target country
4. Enter in the translated search results then click "Search"
5. Click on a result in the local language, then copy the URL of its website
6. Click on "Open Translate", then paste copied URL into translate box
7. Click on the link created in the translate section"""

query = ""

window = tk.Tk()
window.geometry(str(window_shape[0]) + 'x' + str(window_shape[1]))
window.title("International Google Search")
title1 = tk.Label(window, text="International Search", font=("", 12))
search_title = tk.Label(window, text="Enter Search Query:")
loc_title = tk.Label(window, text="Enter Location:")
search = tk.Entry(window, exportselection=0, textvariable=query)

instructions = tk.Label(window, text=instructions_str, justify='left', wraplength=window_shape[0])#, width=window_shape[0])

names = [] #list(searcher.names_to_id.keys())


location_entry = AutocompleteEntry(names, searcher, window)

search_cmd = partial(search_command, search, location_entry, searcher)

search_button = tk.Button(window, text="Search", command=search_cmd)
translate_button = tk.Button(window, text="Open Translate", command=open_translate_command)

# tk.Label(window, text=query).grid(column=0, row=2)
title1.grid(column=0, row=0)

search_title.grid(column=0, row=1)
search.grid(column=0, row=2)
loc_title.grid(column=1, row=1)
location_entry.grid(column=1, row=2)
search_button.grid(column=0, row=6)
translate_button.grid(column=0, row=7)
instructions.grid(row=8, columnspan=2)

window.mainloop()