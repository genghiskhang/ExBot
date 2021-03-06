import json
from os.path import exists

# Returns data.json as a dictionary
def getData():
    with open('assets\\data.json') as file:
        return json.load(file)
    
# Retrieves a player's data in the data.json
def getPlayerData(id):
    with open('assets\\data.json') as file:
        try:
            return json.load(file)['playerInfo'][id]
        except:
            return 'Player not found'

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
        with open('assets\\data.json', 'r') as file:
            if 'playerInfo' not in file.read():
                with open('assets\\data.json', 'w') as file:
                    file.write(json.dumps(base, indent=4))
        return 'data.json already exists'
    
# Creates and appends a data entry of user into data.json if one does not exist already
def initPlayerData(id, playerInfo):
    with open('assets\\data.json') as file:
        data = json.load(file)
        if str(id) in data['playerInfo']:
            return "Player information already exists"
        data['playerInfo'].update(playerInfo)
        print(playerInfo)
    with open('assets\\data.json', 'w') as file:
        file.write(json.dumps(data, indent=4))
    return "Successfully initialized player information"

# Updates a player's data
def updatePlayerData(id, dataKey, newData):
    data = getData()
    data['playerInfo'][str(id)][dataKey] = newData
    with open('assets\\data.json', 'w') as file:
        file.write(json.dumps(data, indent=4))

# Clears a single player's data from JSON
def removePlayerData(id):
    with open('assets\\data.json') as file:
        data = json.load(file)
        data['playerInfo'].pop(str(id))
    with open('assets\\data.json', 'w') as file:
        file.write(json.dumps(data, indent=4))

# Clears all player data from JSON
def clearAllPlayerData():
    with open('assets\\data.json') as file:
        data = json.load(file)
        data['playerInfo'].clear()
    with open('assets\\data.json', 'w') as file:
        file.write(json.dumps(data, indent=4))