import os
import subprocess
import time

def create_and_run_sh(mag_file, layer_name, x_coord, y_coord, sh_filename="temp_script.sh"):
    

    # Kill any previous instances of the magic command using jobs and kill
    try:
        output = subprocess.check_output("jobs -lprs", shell=True).decode('utf-8')
        for line in output.split('\n'):
            print(line)
            if line.strip():  # If line is not empty
                pid = line.strip()  # Assuming the whole line is just the PID
                os.system(f"kill -9 {pid}")
    except subprocess.CalledProcessError:
        pass  # This means that no such process was found or there was an error retrieving the PID

    # Bash script content
    content = f"""#!/bin/bash

magic -noconsole << EOF
load {mag_file}
select
select {layer_name} at {x_coord} {y_coord}
EOF
"""

    # Write content to file
    with open(sh_filename, 'w') as f:
        f.write(content)
    
    # Provide execution permissions
    os.system(f"chmod +x {sh_filename}")

    # Run the magic command using the bash script
    os.system(f"./{sh_filename}")



