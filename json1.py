import json
class File:
    
    def __init__(self,name):
        self.name = name
        d = {"name": "hari", "age":12}
        with open(f"{name}.json","w") as json_file:
            json.dump(d, json_file, indent = 4)
        
    def __repr__(self):
        return "File object created successfully"
    def show_content(self):
            with open(f"{self.name}.json","r") as json_file:
                data = json.load(json_file)
            return data
 
f = File("a")
print(f)
print(f.show_content())

    