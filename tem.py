import json

def extract_and_count_connections(filename):
    # Read the JSON data from the file
    with open(filename, 'r') as f:
        data = json.load(f)

    # Prepare the divisions
    schematic_counts = {}
    layout_counts = {}

    # Iterate through the data
    for item in data:
        if "badnets" in item:
            is_schematic = True  # We start with the assumption that the first list is schematic

            for badnet_set in item["badnets"]:
                if is_schematic:
                    target = schematic_counts
                else:
                    target = layout_counts

                # Count connections for each pin
                for badnet_group in badnet_set:
                    for badnet in badnet_group:
                        pin_name = badnet[0]
                        count = sum([x[2] for x in badnet[1]])
                        
                        if pin_name in target:
                            target[pin_name] += count
                        else:
                            target[pin_name] = count
                
                # Alternate between schematic and layout
                is_schematic = not is_schematic

    return schematic_counts, layout_counts

filename = 'comp1.json'
schematic_counts, layout_counts = extract_and_count_connections(filename)

print("Schematic Counts:", schematic_counts)
print("Layout Counts:", layout_counts)
