def find_label_for_rect(mag_content, x, y,search_type):
    # Split the content into lines
    lines = mag_content.split("\n")
    

    # Start from the end of the file and find the rect which matches
    for i in reversed(range(len(lines))):
        line = lines[i].strip()
        

        # If we find a rect line, check the coordinates
        if line.startswith("rect"):
            rect_coords = list(map(int, line.split()[1:5]))
            if rect_coords[0] <= x <= rect_coords[2] and rect_coords[1] <= y <= rect_coords[3]:
                # If the coordinates are within the rect, find the previous label (header)
                for j in reversed(range(i)):
                    if lines[j].startswith("<<") and lines[j].endswith(">>"):
                        return lines[j][2:-2].strip()  # Remove << >> and return label
                break

    # If we reached here, we did not find the label
    return None

# Prompt the user for the input file name


# Read the content from the provided file

    

# Prompt the user for coordinates



