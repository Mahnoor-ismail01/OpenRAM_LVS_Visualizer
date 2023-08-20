import json

def create_pin_connections(data):
    circuit1 = data['circuit1']
    circuit2 = data['circuit2']
    
    # Assuming both circuits have the same length
    pin_connections = {f"pin_{i+1}": [circuit2[i], circuit1[i]] for i in range(len(circuit1))}
    
    return {"pin_connections": pin_connections}

data = {
    'circuit1': ['Z', 'A', 'gnd', 'vdd_schematic'],
    'circuit2': ['Z', 'A', 'gnd', 'vdd']
}

connections = create_pin_connections(data)

# Saving to output.json
with open("outpi.json", "w") as f:
    json.dump(connections, f, indent=4)

print("Data saved to output.json.")
