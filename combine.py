import json

def extract_key_from_file(filename, key):
    """Extract a specific key's data from a JSON file."""
    with open(filename, "r") as f:
        data = json.load(f)
        return data.get(key, {})

def inputs(pins,nets,devices,pin_connection):
    pins_data = extract_key_from_file(pins, "pins")
    nets_data = extract_key_from_file(nets, "nets")
    devices_data = extract_key_from_file(devices, "device")
    pin_connection = extract_key_from_file(pin_connection, "pin_connections")

    # Combine the data
    combined_data = {
        "pins": pins_data,
        "nets": nets_data,
        "devices": devices_data,
        "pin_connections":pin_connection
    }

    # Write the combined data to a new JSON file
    with open("combined.json", "w") as outfile:
        json.dump(combined_data, outfile, indent=4)

