import json
from os.path import exists

# Returns data.json as a dictionary
def getData():
    with open('assets\\data.json') as file:
        return json.load(file)

# Creates a new data.json file
def createDataJson():
    base = {
        'playerInfo':{
        }
    }
    if not exists('assets\\data.json'):
        open('assets\\data.json', 'x')
        with open('assets\\data.json', 'w') as file:
            file.write(json.dumps(base, indent=4))
        return 'data.json created'
    else:
        return 'data.json already exists'
    
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
            
# Initializes user data into the JSON
def initUser(ctx):
    pass