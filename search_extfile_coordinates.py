import search_lable_magfile
import magic_command
import os
def magic(filename,mag_file,keyword,search_type):
    

    
    def extract_coordinates(filename, keyword, search_type):
        
        with open(filename, 'r') as f:
            for line in f:
                
                if keyword in line:
                    tokens = line.split()
                    try:
                        index = tokens.index(keyword)
                        
                        # Check the search type to determine which coordinates to extract
                        if search_type == "pin":
                        
                            return (int(tokens[index + 2]), int(tokens[index + 3]))
                        elif search_type == "device":

                            return (int(tokens[index + 1]), int(tokens[index + 2]))
                    except (ValueError, IndexError):
                        continue
        return None
    

    
    coordinates = extract_coordinates(filename, keyword, search_type)
    
    
    if coordinates :
        
        
        result=search_lable_magfile.find_label_for_rect(mag_file,coordinates[0],coordinates[1],search_type)
        
        if result:
            
            mag=magic_command.create_and_run_sh(mag_file,result,coordinates[0],coordinates[1])
            return("")


        else:
            
            return("Could not find a matching label.")

    else:
        
        return("Coordinates not found!")
    return("")





