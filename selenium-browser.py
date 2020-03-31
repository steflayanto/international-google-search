import os, time, pyautogui
import selenium

from selenium import webdriver

def country_map():
    code_map = dict()
    code_map["usa"] = 'US'
    code_map["uk"] = 'UK'
    code_map["japan"] = 'JP'
    code_map["spain"]  = "ES"
    code_map["canada"] = 'CA'
    code_map["germany"] = 'DE'
    code_map["italy"] = 'IT'
    code_map["france"] = 'FR'
    code_map["australia"] = 'AU'
    code_map["taiwan"]  = "TW"
    code_map["netherlands"]  = "NL"
    code_map["brasil"] = 'BR'
    code_map["turkey"]  = "TR"
    code_map["belgium"]  = "BE"
    code_map["greece"]  = "GR"
    code_map["india"] = 'IN'
    code_map["mexico"]  = "MX"
    code_map["denmark"]  = "DK"
    code_map["argentina"]  = "AR"
    code_map["switzerland"]  = "CH"
    code_map["chile"]  = "CL"
    code_map["austria"]  = "AT"
    code_map["korea"] = 'KR'
    code_map["ireland"]  = "IE"
    code_map["colombia"]  = "CO"
    code_map["poland"]  = "PL"
    code_map["portugal"]  = "PT"
    code_map["pakistan"] = 'PK'
    return code_map

# STATIC SETTINGS
DPI = 125 # Scaling factor of texts and apps in display settings
screen_dims = [x / (DPI/100) for x in pyautogui.size()]

code_map = country_map()


print("International Google Search")
print("Supported Countries: USA, UK, Japan, Canada, Germany, Italy, France, Australia,  Brasil, India, Korea, Pakistan")

query = input("Please input Search Query: ")
text = " "
codes = []
while text is not "" and len(codes) != 3:
    text = input("Input Country. Input nothing to start search: ").lower()
    if text not in code_map.keys():
        print("\tERROR: Country not recognized")
        continue
    codes.append(code_map[text])
print("Starting Search")

# Using Chrome Incognito to access web
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

drivers = []
for i in range(3):
    drivers.append(webdriver.Chrome(chrome_options=chrome_options))
    drivers[i].set_window_position(i * screen_dims[0] / 3, 0)

assert len(codes) == len(drivers)

for i, driver in enumerate(drivers):
    # Open the website
    code = codes[i]
    driver.get('https://www.google.com/ncr')
    time.sleep(0.5)
    driver.get('https://www.google.com/?gl=' + code)
    # print(screen_dims)
    # print(driver.get_window_size())
    driver.set_window_size(screen_dims[0] / 3, screen_dims[1])
    # print(driver.get_window_size())
    element = driver.find_element_by_name("q")
    element.send_keys(query)
    element.submit()
    
# for i in range(3):
#     drivers[i].set_window_position(i * screen_dims[0] / 3, 0)

# driver.manage().window().setPosition(0,0)

# Get Search Box
# element = driver.find_element_by_name("q")
# element.send_keys("Hotels")
# element.submit()

input("Press enter to exit")