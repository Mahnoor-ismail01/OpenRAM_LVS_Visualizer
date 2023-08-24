import os
import subprocess
import time

def create_and_run_sh(mag_file, layer_name, x_coord, y_coord, sh_filename="temp_script.sh"):
    print(mag_file, layer_name, x_coord, y_coord)
    

   
    

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
    subprocess.Popen(["chmod", "+x", sh_filename])

    # Run the magic command using the bash script
    subprocess.Popen(["./" + sh_filename])



