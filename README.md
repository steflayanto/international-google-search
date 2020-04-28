# International Google Search

A split screen international google search, where each screen would show a google search as if the query were made from a particular countries.

---

## Included Programs

### custom-search-window

Opens up a window allowing you to type in a search query and a location to search from, then opens up the search in a browser window when a button is clicked. Results are returned as if the query was made from the specified location, but with an English interface language. Also can be used to help make searches in local languages to access local sources. Latest version.

### url-appender

An earlier attempt at an international search that opens up a GUI with several predefined buttons (have to be edited directly in code), that searches for an open incognito google search window that is already open to an existing search, then modifies the URL by appending the target country code. Was discontinued due to its bad interface.

### selenium-browser

First attempt at a custom search. Uses the exact same backend URL modification as the url-appender, but opens and manages browsers directly using selenium. Was discontinued because it was too slow.

---

## Dependencies

All code was written and tested in Python 3.7.

### custom-search-window

* Files already included in repository
  * autocomplete_entry.py (taken and modified from <http://code.activestate.com/recipes/578253-an-entry-with-autocompletion-for-the-tkinter-gui/>)
  * location_reference.py
  * url_builder.py

### url-appender

* chromewebdriver (download the executable: required for selenium)
* selenium
* pyautogui
* Files already included in repository
  * location_reference.py

### selenium-browser

* chromewebdriver (download the executable: required for selenium)
* selenium
* pyautogui
* Files already included in repository
  * location_reference.py

# Export Instructions

1. Install pyinstaller using `pip install PyInstaller`
1. Navigate to repository
1. Run command `pyinstaller --onefile --noconsole --add-data="geotargets-2019-02-11.csv;." custom-search-window.py`