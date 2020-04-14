# OUTPUT IN THE FORM OF &uule=w+CAIQICI + <string key> +  ‘Canonical Name’ Base64 format + &cr=country<country ISO code>
# https://blog.linkody.com/seo-local/uule-2
import csv, base64

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

sin = Location()
sin.name = "test"
sin.c_name = "Ras Al-Khaimah,Ras al Khaimah,United Arab Emirates"
sin.country_code = "AE"

url = UrlBuilder("thanks for the warning officer", sin)
print(url.url())