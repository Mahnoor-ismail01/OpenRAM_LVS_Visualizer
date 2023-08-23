import json

def net_json(inputfile):

# Read the input file
    with open(inputfile, "r") as infile:
        data = json.load(infile)

    # Check if the key 'pins' exists in the data and rename it to 'nets'
    if "pins" in data:
        data["nets"] = data.pop("pins")

    # Write the modified data to the output file
    with open("output_nets.json", "w") as outfile:
        json.dump(data, outfile, indent=4)

    print("Modification complete. Check output.json for the result.")
