import json

def extract_key_from_file(filename, key):
    """Extract a specific key's data from a JSON file."""
    with open(filename, "r") as f:
        data = json.load(f)
        return data.get(key, {})

def inputs(pins,nets,devices):
    pins_data = extract_key_from_file(pins, "pins")
    nets_data = extract_key_from_file(nets, "nets")
    devices_data = extract_key_from_file(devices, "device")

    # Combine the data
    combined_data = {
        "pins": pins_data,
        "nets": nets_data,
        "devices": devices_data
    }

    # Write the combined data to a new JSON file
    with open("combined.json", "w") as outfile:
        json.dump(combined_data, outfile, indent=4)

    print("Data combined. Check combined.json for the result.")
