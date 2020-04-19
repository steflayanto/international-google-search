# OUTPUT IN THE FORM OF &uule=w+CAIQICI + <string key> +  ‘Canonical Name’ Base64 format + &cr=country<country ISO code>
# https://blog.linkody.com/seo-local/uule-2
import csv, base64
import webbrowser
from location_reference import *

class UrlBuilder:
    def __init__(self, query, location):
        self.location = location
        self.keys_map = key_map()
        self.query = query
        

    def b64_location(self):
        c_name_bytes = self.location.c_name.encode('ascii')
        base64_bytes = base64.b64encode(c_name_bytes)
        base64_message = base64_bytes.decode('ascii')
        return base64_message

    def url(self):
        out = "https://www.google.com/search?q="
        out += self.query.replace(" ", "+")
        out += "&uule=w+CAIQICI"
        out += self.keys_map[len(self.location.c_name)]
        out += self.b64_location()
        out += "&cr=country"
        out += self.location.country_code
        return out

if __name__ == '__main__':
    loc = Location()
    loc.name = "test"
    loc.c_name = "Ras Al-Khaimah,Ras al Khaimah,United Arab Emirates"
    # loc.c_name = "Pretoria,Gauteng,South Africa"
    # loc.c_name = "Saint Michael,Barbados"
    # loc.country_code = "BB"
    loc.country_code = "AE"

    url = UrlBuilder("elephant seal", loc)
    print(url.url())
    # webbrowser.open_new(url.url())