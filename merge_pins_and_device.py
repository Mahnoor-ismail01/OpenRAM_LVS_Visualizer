import json
def merge_pins(pins_file,device_file):
# Load the JSON files
    with open(pins_file, "r") as f1, open(device_file, "r") as f2:
        json1 = json.load(f1)
        json2 = json.load(f2)

    # Iterate through keys in json1 and lookup in json2
    for values in json1["pins"].values():
        if isinstance(values[-1], dict):
            keys = list(values[-1].keys())
            for key in keys:
                if key in json2["device"]:
                    values[-1][key] = json2["device"][key]

    # Save the updated json1
    with open("final_pins_output.json", "w") as f:
        json.dump(json1, f, indent=4)

    

