import json

with open('comp.json', 'r') as f:
    data = json.load(f)

pins_dict = {'circuit1': [], 'circuit2': []}
devices_dict = {'circuit1': [], 'circuit2': []}
badnets_dict = {'circuit1': {}, 'circuit2': {}}
badelements_dict = {'circuit1': {}, 'circuit2': {}}

# Extracting pins
for entry in data:
    if "pins" in entry:
        for i, circuit_pins in enumerate(entry["pins"]):
            circuit = 'circuit1' if i == 0 else 'circuit2'
            for pin in circuit_pins:
                # Ignore numeric pins
                if not pin.isdigit():
                    pins_dict[circuit].append(pin)

# Extracting devices
for entry in data:
    if "devices" in entry:
        devices_dict['circuit1'].extend(entry["devices"][0])
        devices_dict['circuit2'].extend(entry["devices"][1])

# ... [previous code remains unchanged]

# Extracting badnets
for entry in data:
    if "badnets" in entry:
        badnets_entries = entry["badnets"]

        for idx, badnets_data in enumerate(badnets_entries):
            circuit1_name = 'circuit' + str(2*idx + 1)
            circuit2_name = 'circuit' + str(2*idx + 2)
            
            # Parsing circuit 1 info
            for badnet in badnets_data[0]:
                net_name = badnet[0]
                net_info = badnet[1]

                if circuit1_name not in badnets_dict:
                    badnets_dict[circuit1_name] = {}

                badnets_dict[circuit1_name][net_name] = net_info
            
            # Parsing circuit 2 info
            for badnet in badnets_data[1]:
                net_name = badnet[0]
                net_info = badnet[1]

                if circuit2_name not in badnets_dict:
                    badnets_dict[circuit2_name] = {}

                badnets_dict[circuit2_name][net_name] = net_info

# ... [rest of the code remains unchanged]


# Extracting badelements
for entry in data:
    if "badelements" in entry:
        for i, circuit_badelements in enumerate(entry["badelements"]):
            circuit = 'circuit1' if i == 0 else 'circuit2'
            for badelement in circuit_badelements:
                key = badelement[0][0]
                value = badelement[0][1]
                badelements_dict[circuit][key] = value

print("Pins:", pins_dict)
print("\nDevices:", devices_dict)
print("\nBadnets:", badnets_dict)
print("\nBadelements:", badelements_dict)
