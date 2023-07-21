import json
badelements =[
      [
        [
          [
            "sky130_fd_pr__pfet_01v8:0",
            [
              [ "1", 2 ],
              [ "2", 2 ],
              [ "4", 2 ]
            ]
          ]
        ], [
          [
            "sky130_fd_pr__pfet_01v8:1",
            [
              [ "1", 2 ],
              [ "2", 2 ],
              [ "4", 1 ]
            ]
          ]
        ]
      ]
   ]









def get_pin_dict(component):
    return {pin[0]: pin[1] for pin in component[1]}

def compare_circuits(circuit1, circuit2):
    differences = []
    no_instance_list = []
    
    for (comp1, comp2) in zip(circuit1, circuit2):
        # handle no matching instance case
        if comp2[0] == "(no matching instance)":
            no_instance_list.append((comp1[0], get_pin_dict(comp1)))
            continue

        pin_dict1 = get_pin_dict(comp1)
        pin_dict2 = get_pin_dict(comp2)
        
        for pin_name in pin_dict1.keys():
            if pin_name not in pin_dict2:
                differences.append(f"Pin '{pin_name}' found in first circuit's component '{comp1[0]}' not found in second circuit's component '{comp2[0]}'.")
                continue
            
            if pin_dict1[pin_name] != pin_dict2[pin_name]:
                differences.append(f"Pin '{pin_name}' in component '{comp1[0]}' of first circuit has value {pin_dict1[pin_name]} while in the second circuit's component '{comp2[0]}' it has value {pin_dict2[pin_name]}.")

    return differences, no_instance_list

for circuit_pair in badelements:
    circuit1, circuit2 = circuit_pair
    differences, no_instance_list = compare_circuits(circuit1, circuit2)
    for diff in differences:
        print(diff)
    for no_instance in no_instance_list:
        print(f"No matching instance for '{no_instance[0]}'. First circuit info: {no_instance[1]}")
