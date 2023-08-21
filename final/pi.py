import json

def create_pin_connections(data):
    circuit1 = data['circuit1']
    circuit2 = data['circuit2']
    
    # Assuming both circuits have the same length
    pin_connections = {f"pin_{i+1}": [circuit2[i], circuit1[i]] for i in range(len(circuit1))}
    
    return {"pin_connections": pin_connections}




# Saving to output.json

