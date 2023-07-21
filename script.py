import json

def parse_json_file(file_name):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)

        all_badnets = []
        all_badelements = []
        all_pins = []
        all_properties = []

        badnets_counter = 0
        badelements_counter = 0
        pins_counter = 0
        properties_counter = 0

        for item in data:
            if 'badnets' in item:
                badnets = item['badnets']
                all_badnets.append(badnets)
                badnets_counter += 1

            if 'badelements' in item:
                badelements = item['badelements']
                all_badelements.append(badelements)
                badelements_counter += 1

            if 'pins' in item:
                pins = item['pins']
                all_pins.append(pins)
                pins_counter += 1

            if 'properties' in item:
                properties = item['properties']
                all_properties.append(properties)
                properties_counter += 1

       

        return all_badnets, all_badelements, all_pins, all_properties ,badnets_counter ,badelements_counter, pins_counter ,properties_counter

file_name = "comp_tut6e.json"
all_badnets, all_badelements, all_pins, all_properties,badnets_counter ,badelements_counter, pins_counter ,properties_counter = parse_json_file(file_name)
print("Badnets Count: ", all_badnets)
print("Badelements Count: ", badelements_counter)
print("Pins Count: ", pins_counter)
print("Properties Count: ", properties_counter)
print(len(all_badnets))
a= open("l.txt","w+")
a.write(str(all_badnets))
a.close()