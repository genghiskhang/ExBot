import json
from os.path import exists

# Creates a new data.json file
def createDataJson():
    dict = {
        'playerInfo':{
        }
    }
    if not exists('assets\\data.json'):
        with open('assets\\data.json', 'w') as file:
            file.write(json.dumps(dict, indent=4))
        return 'A data.json file was created'
    else:
        return 'A data.json file already exists'
    
# Creates and appends a data entry of user into data.json if one does not exist already
def initPlayerData(id, playerInfo):
    with open('assets\\data.json') as file:
        oldData = json.load(file)
        if id in oldData['playerInfo']:
            return "Player already exists"
        oldData['playerInfo'].update(playerInfo)
    with open('assets\\data.json', 'w') as file:
        file.write(json.dumps(oldData, indent=4))
    return "Successfully appended player info"

# Clears a single player's data from JSON
# def clearPlayerData(id):
#     with open('assets\\data.json') as file:
#         oldData = json.load(file)
#         oldData['playerInfo'].remove(id)

# Clears all player data from JSON
def clearAllPlayerData():
    with open('assets\\data.json') as file:
        oldData = json.load(file)
        oldData['playerInfo'].clear()
    with open('assets\\data.json', 'w') as file:
        file.write(json.dumps(oldData, indent=4))

dict = {
    "Red":{
        "name":"Exo",
        "id":9511
    }
}

# createDataJson()
# print(initPlayerData('Red', dict))
# clearAllPlayerData()

# Checks if the discord user already has registered info inside the JSON
def checkExisting(userKey):
    with open('assets\\data.json', 'r') as file:
        if userKey in json.load(file):
            return True
    return False
            
# Initializes user data into the JSON
def initUser(ctx):
    pass