import json

def parse_json_file(file_name):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)

        for item in data:
            badnets = item.get('badnets', [])
            badelements = item.get('badelements', [])
            pins = item.get('pins', [])
            properties = item.get('properties', [])

            
            print("badnets: ", badnets)
            print("badelements: ", badelements)
            print("pins: ", pins)
            print("properties: ", properties)
            print("\n---\n") 
parse_json_file("comp.json")
