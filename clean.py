import json

def clean_json(data):
    if isinstance(data, dict):
        new_data = {}
        for key, value in data.items():
            if key == "" or key == "(no matching net)" or value == "" or value == "(no matching net)":
                continue
            if isinstance(value, (dict, list)):
                value = clean_json(value)
            if value not in ["", "(no matching net)"]:
                new_data[key] = value
        return new_data
    elif isinstance(data, list):
        new_list = []
        for item in data:
            cleaned_item = clean_json(item)
            if cleaned_item not in ["", "(no matching net)"]:
                new_list.append(cleaned_item)
        return new_list
    else:
        return data

def main(input_filename,output_filename):
    

    with open(input_filename, 'r') as f:
        data = json.load(f)

    cleaned_data = clean_json(data)

    with open(output_filename, 'w') as f:
        json.dump(cleaned_data, f, indent=4)


