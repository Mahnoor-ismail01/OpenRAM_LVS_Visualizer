def find_label_for_rect(filename, x, y, entity_type):
    #def extract_label_from_magic_file(filename, x, y, entity_type):
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    label = None

    # We use enumerate to loop with both index and the line itself
    for idx, line in enumerate(lines):
        # Clean up the line
        line = line.strip()

        # Check for coordinates in the current line for the pin type
        if entity_type == "pin" and f"rlabel" in line and f"{x} {y}" in line:
            parts = line.split()
            label = parts[1]  # the label after rlabel keyword (like "metal1")
            return label

        # Handle device extraction
        elif entity_type == "device" and f"rect {x} {y}" in line:
            for prev_line in lines[:idx][::-1]:  # search upwards from the current line
                if "<<" in prev_line and ">>" in prev_line:
                    label = prev_line.split(" ")[1]  # Assuming format is always << label >>
                    return label

    return label

# Extract label
result_label = find_label_for_rect("/home/mahnoor/Downloads/INV(changebothother2)/INV.mag", 20, 142, "device")

if result_label:
    print(f"Extracted Label: {result_label}")
else:
    print("Label not found!")
