import pyautogui as gui
import time, pyperclip
import tkinter as tk
from tkinter import messagebox as mb
from location_reference import country_map


# Displays a pop-up error box with a custom message
def error(message):
    mb.showerror("Error", message)

# def callback():
#     if mb.askyesno('Verify', 'Really quit?'):
#         mb.showwarning('Yes', 'Not yet implemented')
#     else:
#         mb.showinfo('No', 'Quit has been cancelled')

# Main function that searches for a search URL box and adds a country parameter to it with the code passed in
def changeCountry(code):
    # print(code)
    pos = None
    i = 0
    timer = time.time()
    while pos is None:
        if time.time() - timer > 3:
            error("Unable to find Google Search on Screen. Make sure a search window is open.")
            return
        pos = gui.locateOnScreen(str(i) + '.png')
        i += 1
        i %= 2

    gui.click(x=pos[0] + 20, y=pos[1] + 10)
    gui.hotkey('ctrl', 'a')
    gui.hotkey('ctrl', 'c')

    search_query = pyperclip.paste()
    # print (search_query)
    if search_query == "https://www.google.com/":
        error("Please search something first.")
        return
    index = search_query.find("&gl=")
    if index is not -1:  # Update code
        search_query = search_query[0:index + 4] +  str(code) + search_query[index + 6:]
    else:
        search_query += "&gl=" + str(code)  # Insert Code

    pyperclip.copy(search_query)
    gui.hotkey('ctrl', 'v')
    gui.press('enter')

map = country_map()
# screen = gui.size()
# print(gui.position())
window = tk.Tk()
window.geometry('300x600')
window.title("International Google Search")
title1 = tk.Label(window, text="International Search", font=("", 12))
title2 = tk.Label(window, text="Select a country:")
title1.grid(column=0, row=0)
title2.grid(column=0, row=1)
pos = 0
for country, code in map.items():
    # print(country, code)
    tk.Button(window, text=country, command=lambda code=code: changeCountry(code)).grid(column= int(pos / 15), row= 3 + (pos % 15))
    pos += 1
# tk.Button(window, text='USA', command=lambda : changeCountry('US')).grid(column=0, row=3)
# tk.Button(window, text='Italy', command=lambda : changeCountry('IT')).grid(column=0, row=4)
# tk.Button(window, text='Italy', command=lambda : changeCountry('IT')).pack(fill=tk.X)
# tk.Button(text='Answer', command=answer).pack(fill=tk.X)
window.mainloop()