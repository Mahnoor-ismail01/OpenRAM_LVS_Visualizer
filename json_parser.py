import json
import pin_connection
import device
import pins
import merge_pins_and_device
import clean
import nets
import combine
import pi
import os
def json_parser(schematic_input,layout_input,jsonfile):
    file_extension = os.path.splitext(jsonfile)[1][1:]
    if file_extension=="json":
   
        with open(jsonfile, 'r') as f:
            data = json.load(f)

        pins_dict = {'circuit1': [], 'circuit2': []}
        devices_dict = {'circuit1': [], 'circuit2': []}
        badnets_dict = {'circuit1': {}, 'circuit2': {}}
        badelements_dict = {'circuit1': {}, 'circuit2': {}}

        def update_badnets_with_pin_connections(pin_connections, badnets_dict):
            for circuit, badnet_info in badnets_dict.items():
                circuit_num = int(circuit[-1])
                
                # Determine whether we are looking at Schematic or Layout
                key = 'Schematic' if circuit_num % 2 == 1 else 'Layout'
                
                for pin_name, badnet_list in badnet_info.items():
                    
                    if pin_name in pin_connections[key]:
                        
                    

                        

                        # Append the pin value at the end of the badnet_list
                        badnet_list.append(pin_connections[key][pin_name])
                    if pin_name not in pin_connections[key]:
                        
                    

                        

                        # Append the pin value at the end of the badnet_list
                        badnet_list.append(0)
                    
                        
            
            return badnets_dict

        def insert_with_count_check(dictionary, key, value):
            if key not in dictionary:
                dictionary[key] = value
            else:
                count = 1
                new_key = f"{key}_{count}"
                while new_key in dictionary:
                    count += 1
                    new_key = f"{key}_{count}"
                dictionary[new_key] = value

        # Extracting pins
        for entry in data:
            if "pins" in entry:
                for i, circuit_pins in enumerate(entry["pins"]):
                    circuit = 'circuit1' if i == 0 else 'circuit2'
                    for pin in circuit_pins:
                        # Ignore numeric pins
                        if not pin.isdigit():
                            pins_dict[circuit].append(pin)

        # Extracting devices
        for entry in data:
            if "devices" in entry:
                devices_dict['circuit1'].extend(entry["devices"][0])
                devices_dict['circuit2'].extend(entry["devices"][1])

        # Extracting badnets
        for entry in data:
            if "badnets" in entry:
                badnets_entries = entry["badnets"]

                for idx, badnets_data in enumerate(badnets_entries):
                    circuit1_name = 'circuit' + str(2*idx + 1)
                    circuit2_name = 'circuit' + str(2*idx + 2)
                    
                    # Parsing circuit 1 info
                    for badnet in badnets_data[0]:
                        net_name = badnet[0]
                        net_info = badnet[1]

                        if circuit1_name not in badnets_dict:
                            badnets_dict[circuit1_name] = {}

                        insert_with_count_check(badnets_dict[circuit1_name], net_name, net_info)
                    
                    # Parsing circuit 2 info
                    for badnet in badnets_data[1]:
                        net_name = badnet[0]
                        net_info = badnet[1]

                        if circuit2_name not in badnets_dict:
                            badnets_dict[circuit2_name] = {}

                        insert_with_count_check(badnets_dict[circuit2_name], net_name, net_info)

        # Extracting badelements
        for entry in data:
            if "badelements" in entry:
                for i, circuit_badelements in enumerate(entry["badelements"]):
                    circuit = 'circuit1' if i == 0 else 'circuit2'
                    for badelement in circuit_badelements:
                        key = badelement[0][0]
                        value = badelement[0][1]
                        insert_with_count_check(badelements_dict[circuit], key, value)
        schematic_pin=pin_connection.parse_netlist(schematic_input)
        layout_pin=pin_connection.parse_netlist(layout_input)
        pin_connection_both={
            "Schematic": schematic_pin,
            "Layout": layout_pin
        }
        a=update_badnets_with_pin_connections(pin_connection_both,badnets_dict)#pin connection count
        device_data_processed=device.extract_connections(badnets_dict)#device data prcessing
        device_data_json=device.create_json_from_processed_data(device_data_processed)#make json of device
        #pins
        pins_data_processed=badnets_dict
        circuit1_data, circuit2_data = pins.aggregate_data(pins_data_processed)
        badnets_dict = {'circuit1': circuit1_data, 'circuit2': circuit2_data}
        pins_data_processed=pins.process(badnets_dict)
        pins_data_json=pins.generate_json_output(pins_data_processed)
        #merge pins 
        merge=merge_pins_and_device.merge_pins("output_pins.json","output_device.json")
        #clean empty strings
        cleann_pin=clean.main("final_pins_output.json","final_pins_output.json")
        cleann_device=clean.main("output_device.json","output_device.json")
        #nets
        netss=nets.net_json("final_pins_output.json")

        #pinsssslast
        con=pi.create_pin_connections(pins_dict)
        with open("outpi.json", "w") as f:
            json.dump(con, f, indent=4)

    

        #create final json that include pins,nets, and devices.
        final_json=combine.inputs("final_pins_output.json","output_nets.json","output_device.json","outpi.json")
        

            


        print("Pins:", pins_dict)
        print("\nDevices:", devices_dict)
        print("\nBadnets:", badnets_dict)
        print("\nBadelements:", badelements_dict)
        return("")

    else:
        return("Invalid Input..! Please enter json file")
