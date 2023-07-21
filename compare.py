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

    # Check for missing, device difference
    for circuit1_net in circuit1:
        if circuit1_net[0] == "(no matching net)":
            continue  # Skip this net, don't consider it missing
        for pin_info1 in circuit1_net[1]:
            found_in_c2 = False
            for circuit2_net in circuit2:
                if circuit1_net[0] == circuit2_net[0]:  # Matching net names
                    for pin_info2 in circuit2_net[1]:
                        if len(pin_info1) > 1 and len(pin_info2) > 1 and pin_info1[0] == pin_info2[0]:  # Check each pin
                            found_in_c2 = True
                            if len(pin_info1) > 2 and len(pin_info2) > 2 and pin_info1[2] != pin_info2[2]:  # Different devices
                                device_diff.append([circuit1_net[0], pin_info2, pin_info1[2]])  # Add circuit2 info and circuit1 device count to the device_diff list
                            break
                if found_in_c2:
                    break
            if not found_in_c2:  # If pin_info1 is not in any of circuit2_net
                missing_nets.append([circuit1_net[0], pin_info1])  # this pin is in circuit1_net but not in the corresponding circuit2_net

    # Check for extra and unknown nets
    for circuit2_net in circuit2:
        found_in_c1 = False
        for circuit1_net in circuit1:
            if circuit1_net[0] == circuit2_net[0]:  # Matching net names
                found_in_c1 = True
                for pin_info2 in circuit2_net[1]:
                    found_in_c1_net = any(len(pin_info1) > 1 and pin_info1[0] == pin_info2[0] and pin_info1[1] == pin_info2[1] for pin_info1 in circuit1_net[1])  # Check each pin and its connections
                    if not found_in_c1_net:  # If pin_info2 is not in circuit1_net
                        unknown_nets.append([circuit2_net[0], pin_info2])  # this pin is in circuit2_net but not in the corresponding circuit1_net
                break
        if not found_in_c1:  # If circuit2_net is not in circuit1
            if circuit2_net[0] != "(no matching net)":  # Ignore placeholder net
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


badnets = [
      [
        [
          [
            "(no matching net)",
            [
              [ "", "", 0 ]
            ]
          ]
        ], [
          [
            "gnd",
            [
              [ "sky130_fd_sc_hd__inv_1", "VGND", 6 ],
              [ "sky130_fd_sc_hd__inv_1", "VNB", 6 ],
              [ "sky130_fd_sc_hd__inv_1", "VPB", 6 ],
              [ "sky130_fd_sc_hd__inv_1", "VPWR", 6 ],
              [ "sky130_fd_sc_hd__nand2_1", "VGND", 1 ],
              [ "sky130_fd_sc_hd__nand2_1", "VNB", 1 ],
              [ "sky130_fd_sc_hd__nand2_1", "VPB", 1 ],
              [ "sky130_fd_sc_hd__nand2_1", "VPWR", 1 ],
              [ "sky130_fd_sc_hd__mux2_1", "VGND", 1 ],
              [ "sky130_fd_sc_hd__mux2_1", "VNB", 1 ],
              [ "sky130_fd_sc_hd__mux2_1", "VPB", 1 ],
              [ "sky130_fd_sc_hd__mux2_1", "VPWR", 1 ]
            ]
          ]
        ]
      ],
      [
        [
          [
            "vdd",
            [
              [ "sky130_fd_sc_hd__mux2_1", "VPB", 1 ],
              [ "sky130_fd_sc_hd__mux2_1", "VPWR", 1 ],
              [ "sky130_fd_sc_hd__nand2_1", "VPB", 1 ],
              [ "sky130_fd_sc_hd__nand2_1", "VPWR", 1 ],
              [ "sky130_fd_sc_hd__inv_1", "VPB", 6 ],
              [ "sky130_fd_sc_hd__inv_1", "VPWR", 6 ]
            ]
          ],
          [
            "gnd",
            [
              [ "sky130_fd_sc_hd__mux2_1", "VGND", 1 ],
              [ "sky130_fd_sc_hd__mux2_1", "VNB", 1 ],
              [ "sky130_fd_sc_hd__nand2_1", "VGND", 1 ],
              [ "sky130_fd_sc_hd__nand2_1", "VNB", 1 ],
              [ "sky130_fd_sc_hd__inv_1", "VGND", 6 ],
              [ "sky130_fd_sc_hd__inv_1", "VNB", 6 ]
            ]
          ]
        ], [
          [
            "(no matching net)",
            [
              [ "", "", 0 ]
            ]
          ],
          [
            "(no matching net)",
            [
              [ "", "", 0 ]
            ]
          ]
        ]
      ],
      [
        [
          [
            "EN",
            [
              [ "sky130_fd_sc_hd__nand2_1", "A", 1 ]
            ]
          ],
          [
            "SEL",
            [
              [ "sky130_fd_sc_hd__mux2_1", "S", 1 ]
            ]
          ]
        ], [
          [
            "SEL",
            [
              [ "sky130_fd_sc_hd__mux2_1", "S", 1 ]
            ]
          ],
          [
            "EN",
            [
              [ "sky130_fd_sc_hd__nand2_1", "A", 1 ]
            ]
          ]
        ]
      ],
      [
        [
          [
            "N3",
            [
              [ "sky130_fd_sc_hd__inv_1", "Y", 1 ],
              [ "sky130_fd_sc_hd__inv_1", "A", 1 ]
            ]
          ],
          [
            "OUT",
            [
              [ "sky130_fd_sc_hd__inv_1", "Y", 1 ],
              [ "sky130_fd_sc_hd__inv_1", "A", 1 ]
            ]
          ],
          [
            "N0",
            [
              [ "sky130_fd_sc_hd__nand2_1", "Y", 1 ],
              [ "sky130_fd_sc_hd__inv_1", "A", 1 ]
            ]
          ],
          [
            "A",
            [
              [ "sky130_fd_sc_hd__mux2_1", "X", 1 ],
              [ "sky130_fd_sc_hd__nand2_1", "B", 1 ]
            ]
          ],
          [
            "N6",
            [
              [ "sky130_fd_sc_hd__mux2_1", "A1", 1 ],
              [ "sky130_fd_sc_hd__inv_1", "Y", 1 ]
            ]
          ]
        ], [
          [
            "sky130_fd_sc_hd__inv_1_3/Y",
            [
              [ "sky130_fd_sc_hd__mux2_1", "A1", 1 ],
              [ "sky130_fd_sc_hd__inv_1", "Y", 1 ]
            ]
          ],
          [
            "sky130_fd_sc_hd__inv_1_1/A",
            [
              [ "sky130_fd_sc_hd__inv_1", "A", 1 ],
              [ "sky130_fd_sc_hd__inv_1", "Y", 1 ]
            ]
          ],
          [
            "sky130_fd_sc_hd__mux2_1_0/X",
            [
              [ "sky130_fd_sc_hd__nand2_1", "B", 1 ],
              [ "sky130_fd_sc_hd__mux2_1", "X", 1 ]
            ]
          ],
          [
            "OUT",
            [
              [ "sky130_fd_sc_hd__inv_1", "Y", 1 ],
              [ "sky130_fd_sc_hd__inv_1", "A", 1 ]
            ]
          ],
          [
            "sky130_fd_sc_hd__inv_1_4/A",
            [
              [ "sky130_fd_sc_hd__inv_1", "A", 1 ],
              [ "sky130_fd_sc_hd__nand2_1", "Y", 1 ]
            ]
          ]
        ]
      ],
      [
        [
          [
            "N4",
            [
              [ "sky130_fd_sc_hd__inv_1", "Y", 1 ],
              [ "sky130_fd_sc_hd__inv_1", "A", 1 ]
            ]
          ],
          [
            "N5",
            [
              [ "sky130_fd_sc_hd__inv_1", "Y", 1 ],
              [ "sky130_fd_sc_hd__inv_1", "A", 1 ]
            ]
          ]
        ], [
          [
            "(no matching net)",
            [
              [ "", "", 0 ]
            ]
          ],
          [
            "(no matching net)",
            [
              [ "", "", 0 ]
            ]
          ]
        ]
      ],
      [
        [
          [
            "(no matching net)",
            [
              [ "", "", 0 ]
            ]
          ],
          [
            "(no matching net)",
            [
              [ "", "", 0 ]
            ]
          ]
        ], [
          [
            "sky130_fd_sc_hd__inv_1_2/A",
            [
              [ "sky130_fd_sc_hd__inv_1", "Y", 1 ],
              [ "sky130_fd_sc_hd__inv_1", "A", 1 ]
            ]
          ],
          [
            "sky130_fd_sc_hd__inv_1_3/A",
            [
              [ "sky130_fd_sc_hd__inv_1", "Y", 1 ],
              [ "sky130_fd_sc_hd__inv_1", "A", 1 ]
            ]
          ]
        ]
      ],
      [
        [
          [
            "N2",
            [
              [ "sky130_fd_sc_hd__mux2_1", "A0", 1 ],
              [ "sky130_fd_sc_hd__inv_1", "Y", 1 ],
              [ "sky130_fd_sc_hd__inv_1", "A", 1 ]
            ]
          ]
        ], [
          [
            "sky130_fd_sc_hd__inv_1_5/Y",
            [
              [ "sky130_fd_sc_hd__inv_1", "Y", 1 ],
              [ "sky130_fd_sc_hd__inv_1", "A", 1 ],
              [ "sky130_fd_sc_hd__mux2_1", "A0", 1 ]
            ]
          ]
        ]
      ]
   ]

extract_and_compare_deep_general(badnets)
