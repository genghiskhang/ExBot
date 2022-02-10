import json
from os.path import exists

from prometheus_client import Info

# Creates a new data.json file
def createDataJson():
    if not exists('assets\\data.json'):
        with open('assets\\data.json', 'w') as file:
            dict = {
                'playerInfo':{
                    
                }
            }
            file.write(json.dumps(dict, indent=4))
        return 'A data.json file was created'
    else:
        return 'A data.json file already exists'
    
def addData(info):
    with open('assets\\data.json', 'r+') as file:
        currentJson = json.load(file)
        currentJson.update(info)
        json.dump(currentJson, file)

print(createDataJson())
addData()

# Checks if the discord user already has registered info inside the JSON
def checkExisting(userKey):
    with open('assets\\data.json', 'r') as file:
        if userKey in json.load(file):
            return True
    return False
            
# Initializes user data into the JSON
def initUser(ctx):
    pass