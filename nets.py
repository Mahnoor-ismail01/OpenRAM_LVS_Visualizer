import json



def merge_data(base_data, additional_data, circuit_name):
    for net, connections in additional_data.items():
        for connection in connections:
            component, pin, _ = connection
            if component not in base_data:
                base_data[component] = {}
            if circuit_name not in base_data[component]:
                base_data[component][circuit_name] = {}
            if net not in base_data[component][circuit_name]:
                base_data[component][circuit_name][net] = []
            base_data[component][circuit_name][net].append(pin)

def extract_connections(badnets):
    result = {
        "circuit1": {},
        "circuit2": {}
    }

    # Pre-process to create a list of keys for circuit2 (even numbers)
    circuit2_keys = [key for key in badnets.keys() if int(key[-1]) % 2 == 0]

    for circuit_key in circuit2_keys:
        circuit1_key = f"circuit{int(circuit_key[-1]) - 1}"

        # Extract circuit2 data
        data_c2 = badnets.get(circuit_key, {})
        
        for net, connections in data_c2.items():
            for connection in connections:
                # Check if connection is iterable and has at least two items
                if isinstance(connection, (list, tuple)) and len(connection) >= 2:
                    component, pin, _ = connection
                    if component not in result["circuit2"]:
                        result["circuit2"][component] = {}
                    if net not in result["circuit2"][component]:
                        result["circuit2"][component][net] = []
                    result["circuit2"][component][net].append(pin)

        # Extract circuit1 data directly without trying to match with circuit2
        data_c1 = badnets.get(circuit1_key, {})
        
        for net, connections in data_c1.items():
            for connection in connections:
                # Check if connection is iterable and has at least two items
                if isinstance(connection, (list, tuple)) and len(connection) >= 2:
                    component, pin, _ = connection
                    if component not in result["circuit1"]:
                        
                        result["circuit1"][component] = {}
                    if net not in result["circuit1"][component]:
                        result["circuit1"][component][net] = []
                    result["circuit1"][component][net].append(pin)


    return result


def sort_based_on_reference(source, reference):
    source_list = list(source)
    reference_list = list(reference)
    sorted_source = sorted(source_list, key=lambda x: reference_list.index(x) if x in reference_list else float('inf'))
    extra_keys = [k for k in reference_list if k not in source_list]
    sorted_source.extend(extra_keys)
    return sorted_source

def create_json_from_processed_data(data):
    circuit1_data = data['circuit1']
    circuit2_data = data['circuit2']

    circuit1_sorted_keys = sort_based_on_reference(circuit1_data, circuit2_data)

    result = {"device": {}}

    for device_name_c2 in circuit1_sorted_keys:
        device_pins_c1 = circuit1_data.get(device_name_c2, {})
        device_pins_c2 = circuit2_data.get(device_name_c2, {})

        pin_data = {}
        all_pins = set(device_pins_c1.keys()) | set(device_pins_c2.keys())

        for pin_name in all_pins:
            pin_name_c2 = "0" if pin_name not in device_pins_c2 else pin_name
            pin_connections_c1 = device_pins_c1.get(pin_name, [])
            pin_connections_c2 = device_pins_c2.get(pin_name_c2, [])

            connection_data = {}
            all_connections = set(pin_connections_c1) | set(pin_connections_c2)
            for conn in all_connections:
                connection_c1_value = conn if conn in pin_connections_c1 else "0"
                connection_c2_value = conn if conn in pin_connections_c2 else "0"
                connection_data[connection_c2_value] = [connection_c2_value, connection_c1_value]

            pin_data_key = pin_name_c2
            pin_data[pin_data_key] = [pin_name_c2, pin_name, connection_data]

        result_key = device_name_c2
        result["device"][result_key] = [device_name_c2, device_name_c2 if device_name_c2 in circuit1_data else "0", pin_data]

    with open("output.json", "w") as outfile:
        json.dump(result, outfile, indent=4)

    return result
# Test data
badnets = {'circuit1': {'Z': [['sky130_fd_pr__pfet_01v8', '1|3', 1], ['sky130_fd_pr__nfet_01v8', '1|3', 1], 3], 'A': [['sky130_fd_pr__pfet_01v8', '2', 1], ['sky130_fd_pr__nfet_01v8', '2', 1], 3], 'vdd': [['sky130_fd_pr__pfet_01v8', '1|3', 1], ['sky130_fd_pr__pfet_01v8', '4', 1], 3]}, 'circuit2': {'vdd': [['sky130_fd_pr__nfet_01v8', '1|3', 1], ['sky130_fd_pr__nfet_01v8', '2', 1], ['sky130_fd_pr__pfet_01v8', '1|3', 2], ['sky130_fd_pr__pfet_01v8', '2', 1], ['sky130_fd_pr__pfet_01v8', '4', 1], 7], '(no matching net)': [['', '', 0], 0], '(no matching net)_1': [['', '', 0], 0]}}
formatted_data = extract_connections(badnets)

a=create_json_from_processed_data(formatted_data)
print(formatted_data)
