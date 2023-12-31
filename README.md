# Google Summer of Code 2023



<center><a href=""><img src="https://developers.google.com/open-source/gsoc/resources/downloads/GSoC-logo-horizontal.svg" alt="gsoc" height="50" width="400"/><img src="image/ospo.png" height ="50" widht="400"/> </a></center> 


# OpenRAM LVS Visualizer

OpenRAM Layout Vs Schematic Netlist Visualizer Desktop Application.

Developed by <b>Mahnoor Ismail</b> 

This is developed purely in Python Programming Language. GUI is supported by PyQt5 Framework.

This Project was created as part of Google Summer of Code 2023 Programme for Open Source Contribution.

| Organization | University of California - Open Source Program Office (UC-OSPO) |
|--------------|-----------:|
| Mentors | Jesse Cirimelli-Low and Matthew Guthaus |
| Contributor | Mahnoor Ismail |

## Short Description
The "LVS Visualizer" is a tool designed to aid in the comparison of schematic and layout netlists in circuit design. With its intuitive graphical interface, users can effortlessly spot discrepancies between a circuit's layout and its schematic. A standout feature is its interactive capability: clicking on a net, device, or pin immediately highlights it in the layout in magic, allowing users to swiftly locate and address any mismatches. This application streamlines the process of analyzing and correcting circuit layout issues, ensuring fidelity to the original schematics.

### How to Run

Install Python libraries (ONE TIME)
```ruby
pip install -r requirements.txt
```

Direct GUI Launch
```ruby
python lvs.py
OR
python3 lvs.py
```

[Optional] Provide command line arguments. Following are the supported arguments.

```ruby
mahnoor@mahnoor-Inspiron-14-5425:~/Downloads/LVS_Mismatch$ python3 lvs.py -h
usage: lvs.py [-h] [-s SCHEMATIC_NETLIST] [-l LAYOUT_NETLIST] [-j JSON_OUTPUT] [-m MAGIC_FILE] [-e EXT_FILE]

Process some netlists and files.

options:
  -h, --help            show this help message and exit
  -s SCHEMATIC_NETLIST, --schematic_netlist SCHEMATIC_NETLIST
                        Path to schematic netlist
  -l LAYOUT_NETLIST, --layout_netlist LAYOUT_NETLIST
                        Path to layout netlist
  -j JSON_OUTPUT, --json_output JSON_OUTPUT
                        Path to JSON output file
  -m MAGIC_FILE, --magic_file MAGIC_FILE
                        Path to magic file
  -e EXT_FILE, --ext_file EXT_FILE
                        Path to EXT file
```

An example run with arguments
```ruby
python3 lvs.py -s /home/mahnoor/Downloads/INV/INV.cdl -l /home/mahnoor/Downloads/INV/INV.spice -j /home/mahnoor/Downloads/INV/comp.json -m /home/mahnoor/Downloads/INV/INV.mag -e /home/mahnoor/Downloads/INV/INV.ext
```

You can also give half arguments through command line and rest using the GUI Browse option. An example:

```ruby
python3 lvs.py -s /home/mahnoor/Downloads/INV/INV.cdl -l /home/mahnoor/Downloads/INV/INV.spice
```

## Prerequisites
What needs to be installed before running the application.
- python3
- pyqt5
- magic
