import os
import subprocess
import time

def create_and_run_sh(mag_file, layer_name, x_coord, y_coord, sh_filename="temp_script.sh"):
    

   
    try:
        output = subprocess.check_output("jobs -lprs", shell=True).decode('utf-8')
        for line in output.split('\n'):
            print(line)
            if line.strip():  
                pid = line.strip()  
                os.system(f"kill -9 {pid}")
    except subprocess.CalledProcessError:
        pass  

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



