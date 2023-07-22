def extract_and_compare_deep_general(badnets):
    for set_num, circuit_set in enumerate(badnets):
        for i in range(1, len(circuit_set)):
            print(f"\nCircuit {i + 1}:")
            missing_nets, extra_nets, unknown_nets, device_diff = compare_circuits(circuit_set[0], circuit_set[i])
            print_info(missing_nets, extra_nets, unknown_nets, device_diff)
def compare_circuits(circuit1, circuit2):
    missing_nets = []
    extra_nets = []
    unknown_nets = []
    device_diff = []

    
    for circuit1_net in circuit1:
        if circuit1_net[0] == "(no matching net)":
            continue  
        for pin_info1 in circuit1_net[1]:
            found_in_c2 = False
            for circuit2_net in circuit2:
                if circuit1_net[0] == circuit2_net[0]:  
                    for pin_info2 in circuit2_net[1]:
                        if len(pin_info1) > 1 and len(pin_info2) > 1 and pin_info1[0] == pin_info2[0]:  
                            found_in_c2 = True
                            if len(pin_info1) > 2 and len(pin_info2) > 2 and pin_info1[2] != pin_info2[2]:  
                                device_diff.append([circuit1_net[0], pin_info2, pin_info1[2]])  
                            break
                if found_in_c2:
                    break
            if not found_in_c2:  
                missing_nets.append([circuit1_net[0], pin_info1])  

    
    for circuit2_net in circuit2:
        found_in_c1 = False
        for circuit1_net in circuit1:
            if circuit1_net[0] == circuit2_net[0]: 
                found_in_c1 = True
                for pin_info2 in circuit2_net[1]:
                    found_in_c1_net = any(len(pin_info1) > 1 and pin_info1[0] == pin_info2[0] and pin_info1[1] == pin_info2[1] for pin_info1 in circuit1_net[1])  
                    if not found_in_c1_net:  
                        unknown_nets.append([circuit2_net[0], pin_info2])  
                break
        if not found_in_c1:  
            if circuit2_net[0] != "(no matching net)":  
                extra_nets.append(circuit2_net)

    return missing_nets, extra_nets, unknown_nets, device_diff




def print_info(missing_nets, extra_nets, unknown_nets, device_diff):
    if missing_nets:
        print("Missing nets:")
        for net in missing_nets:
            print(net)

    if extra_nets:
        print("Extra nets:")
        for net in extra_nets:
            print(net)

    if unknown_nets:
        print("Unknown nets:")
        for net in unknown_nets:
            print(net)

    if device_diff:
        print("Device differences:")
        for diff in device_diff:
            print(f"In Circuit 2: Net '{diff[0]}', Device '{diff[1][0]}', Connections '{diff[1][1]}', Count {diff[1][2]}")
            print(f"In Circuit 1: Count {diff[2]} for the same net and device")
