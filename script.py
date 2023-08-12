import json
import compare
import badelement

def keep_duplicates(ordered_pairs):
    d = {}
    for k, v in ordered_pairs:
        if k in d:
            if type(d[k]) is list:
                d[k].append(v)
            else:
                d[k] = [d[k], v]
        else:
            d[k] = v
    return d

def parse_json_file(file_name):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file, object_pairs_hook=keep_duplicates)

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
                if type(badnets) is list:
                    all_badnets.extend(badnets)
                    badnets_counter += len(badnets)
                else:
                    all_badnets.append(badnets)
                    badnets_counter += 1

            if 'badelements' in item:
                badelements = item['badelements']
                if type(badelements) is list:
                    all_badelements.extend(badelements)
                    badelements_counter += len(badelements)
                else:
                    all_badelements.append(badelements)
                    badelements_counter += 1

            if 'pins' in item:
                pins = item['pins']
                if type(pins) is list:
                    all_pins.extend(pins)
                    pins_counter += len(pins)
                else:
                    all_pins.append(pins)
                    pins_counter += 1

            if 'properties' in item:
                properties = item['properties']
                if type(properties) is list:
                    all_properties.extend(properties)
                    properties_counter += len(properties)
                else:
                    all_properties.append(properties)
                    properties_counter += 1

        return all_badnets, all_badelements, all_pins, all_properties ,badnets_counter ,badelements_counter, pins_counter ,properties_counter

file_name = "comp1.json"
all_badnets, all_badelements, all_pins, all_properties, badnets_counter, badelements_counter, pins_counter, properties_counter = parse_json_file(file_name)


if len(all_badnets)>0:
    if badnets_counter != 1:
        
        for i in range(len(all_badnets)):
            if i==0:
                l=[]
                a=l.append(all_badnets[0])
                compare.extract_and_compare_deep_general(l)

            else:
                compare.extract_and_compare_deep_general(all_badnets[i])
    else:
        compare.extract_and_compare_deep_general(all_badnets)

if len(all_badelements)>0:
    
    
    
    if badelements_counter != 1:
        
        for i in range(len(all_badelements)):
            if i==0:
            
           
          
            
                l=[]
                a=l.append(all_badelements[i])
                print(l)
                badelement.main(l)
            else:
                
                badelement.main(all_badelements[i])

    else:
        
        badelement.main(all_badelements)

