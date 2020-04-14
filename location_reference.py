import csv

def key_map():
    len_to_key = dict()
    len_to_key[4] = 'E'
    len_to_key[5] = 'F'
    len_to_key[6] = 'G'
    len_to_key[7] = 'H'
    len_to_key[8] = 'I'
    len_to_key[9] = 'J'
    len_to_key[10] = 'K'
    len_to_key[11] = 'L'
    len_to_key[12] = 'M'
    len_to_key[13] = 'N'
    len_to_key[14] = 'O'
    len_to_key[15] = 'P'
    len_to_key[16] = 'Q'
    len_to_key[17] = 'R'
    len_to_key[18] = 'S'
    len_to_key[19] = 'T'
    len_to_key[20] = 'U'
    len_to_key[21] = 'V'
    len_to_key[22] = 'W'
    len_to_key[23] = 'X'
    len_to_key[24] = 'Y'
    len_to_key[25] = 'Z'
    len_to_key[26] = 'a'
    len_to_key[27] = 'b'
    len_to_key[28] = 'c'
    len_to_key[29] = 'd'
    len_to_key[30] = 'e'
    len_to_key[31] = 'f'
    len_to_key[32] = 'g'
    len_to_key[33] = 'h'
    len_to_key[34] = 'i'
    len_to_key[35] = 'j'
    len_to_key[36] = 'k'
    len_to_key[37] = 'l'
    len_to_key[38] = 'm'
    len_to_key[39] = 'n'
    len_to_key[40] = 'o'
    len_to_key[41] = 'p'
    len_to_key[42] = 'q'
    len_to_key[43] = 'r'
    len_to_key[44] = 's'
    len_to_key[45] = 't'
    len_to_key[46] = 'u'
    len_to_key[47] = 'v'
    len_to_key[48] = 'w'
    len_to_key[49] = 'x'
    len_to_key[50] = 'y'
    len_to_key[51] = 'z'
    len_to_key[52] = '0'
    len_to_key[53] = '1'
    len_to_key[54] = '2'
    len_to_key[55] = '3'
    len_to_key[56] = '4'
    len_to_key[57] = '5'
    len_to_key[58] = '6'
    len_to_key[59] = '7'
    len_to_key[60] = '8'
    len_to_key[61] = '9'
    len_to_key[62] = '-'
    len_to_key[63] = ' '
    len_to_key[64] = 'A'
    len_to_key[65] = 'B'
    len_to_key[66] = 'C'
    len_to_key[67] = 'D'
    len_to_key[68] = 'E'
    len_to_key[69] = 'F'
    len_to_key[70] = 'G'
    len_to_key[71] = 'H'
    len_to_key[72] = 'I'
    len_to_key[73] = 'J'
    len_to_key[76] = 'M'
    len_to_key[83] = 'T'
    len_to_key[89] = 'L'
    return len_to_key

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
    code_map["brazil"] = 'BR'
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

class Location:
    def __init__ (self):
        self.id = None              # Criteria ID
        self.name = None            # Name
        self.c_name = None          # Canonical Name
        self.parent_id = None       # Parent ID
        self.country_code = None    # Country Code
        self.target_type = None     # Target Type
        self.status = None          # Status
    
    def full_string(self):
        out = str(self)
        if self.target_type is not None:
            out += "\tType: " + self.target_type
        if self.status is not None:
            out += " Status: " + self.status
        if self.id is not None:
            out += " ID: " + self.id
        if self.parent_id is not None:
            out += " Parent ID " + self.parent_id
        return out

    def __str__(self):
        out = ""
        if self.name is not None:
            out += self.name
        if self.country_code is not None:
            out += ", " +  self.country_code
        if self.c_name is not None:
            out += ": " + self.c_name
        return out
        


class LocationSearcher:
    def __init__(self, filename):
        self.id_to_loc = dict()
        # self.name_to_id = dict()
        # self.c_name_to_id = dict()
        self.names_to_id = dict()
        with open(filename, newline='\n', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile)
            try:
                for line in reader:
                    if line[1] == 'Name':
                        continue
                    
                    loc = Location()
                    loc.id, loc.name, loc.c_name, loc.parent_id, loc.country_code, loc.target_type, loc.status = line
                    self.id_to_loc[loc.id] = loc
                    self.names_to_id[loc.name] = loc.id
                    self.names_to_id[loc.c_name] = loc.id
                    # self.name_to_id[loc.name] = loc.id
                    # self.c_name_to_id[loc.c_name] = loc.id
            except  Exception as inst:
                print(type(inst))
                print(inst.args)
                print(inst)
                print("ERROR in Import")

    def search(self, input):
        matches = []
        input = input.lower()
        for name in self.names_to_id.keys():
            if input in name.lower():
                if name.lower().startswith(input):
                    matches.insert(0, name)
                else:
                    matches.append(name)
        
        # for name in self.c_name_to_id.keys():
        #     if name.lower().startswith(input):
        #         if name.lower().startswith(input):
        #             matches.insert(0, name)
        #         else:
        #             matches.append(name)
        return matches

    def check_name(self, name):
        return name in self.names_to_id.keys()

    def get_id(self, name):
        if self.check_name(name):
            return self.names_to_id[name]
        else:
            print("Error: Invalid Name")
    
    def get_loc_by_id(self, id):
        if id in self.id_to_loc.keys():
            return self.id_to_loc[id]
        else:
            print("Error: Invalid ID")

if __name__ == "__main__":
    searcher = LocationSearcher("geotargets-2019-02-11.csv")
    # for id, loc in searcher.id_to_loc.items():
    #     print(loc)

    query = input("Search Regions: ")
    res = searcher.search(query)
    print(res)
    name = input("Pick Area: ")

    if searcher.check_name(name):
        id = searcher.get_id(name)
        loc = searcher.get_loc_by_id(id)
        print(loc.full_string())
