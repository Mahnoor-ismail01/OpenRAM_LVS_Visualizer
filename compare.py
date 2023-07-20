def extract_and_compare_deep_general(badnets):
    # Iterate over each set of circuits
    for set_num, circuit_set in enumerate(badnets):
        print(f"Processing circuit set {set_num + 1}...")

        # Extracting the 'badnets' of each Circuit in the set
        for i in range(1, len(circuit_set)):
            print(f"Circuit {i + 1} info: ", circuit_set[i])

            # Checking for mismatches by comparing each Circuit with the first one in the set
            for circuit1_net in circuit_set[0]:
                found = False
                for circuit2_net in circuit_set[i]:
                    if circuit2_net[0] == circuit1_net[0]:  # same net found
                        found = True
                        for pin_info in circuit2_net[1]:  # check each pin info
                            if pin_info not in circuit1_net[1]:  # if not present in Circuit 1
                                print(f"Mismatch in {circuit2_net[0]} in Circuit {i + 1} compared to Circuit 1: ", pin_info)
                        break  # move to next circuit2_net after match is found
                if not found:
                    if circuit1_net[0] != '(no matching net)':
                        print(f"{circuit1_net[0]} not found in Circuit {i + 1}")
                    else:
                        print(f"No matching net found in Circuit {i + 1} for {circuit1_net[0]} in Circuit 1. Details: ", circuit1_net[1])

badnets = [
      [
        [
          [
            "Z",
            [
              [ "sky130_fd_pr__pfet_01v8", "1|3", 1 ],
              [ "sky130_fd_pr__nfet_01v8", "1|3", 1 ]
            ]
          ],
          [
            "A",
            [
              [ "sky130_fd_pr__pfet_01v8", "2", 1 ],
              [ "sky130_fd_pr__nfet_01v8", "2", 1 ]
            ]
          ],
          [
            "vdd",
            [
              [ "sky130_fd_pr__pfet_01v8", "1|3", 1 ],
              [ "sky130_fd_pr__pfet_01v8", "4", 1 ]
            ]
          ]
        ], [
          [
            "Z",
            [
              [ "sky130_fd_pr__nfet_01v8", "1|3", 1 ],
              [ "sky130_fd_pr__pfet_01v8", "1|3", 1 ]
            ]
          ],
          [
            "A",
            [
              [ "sky130_fd_pr__nfet_01v8", "2", 1 ],
              [ "sky130_fd_pr__pfet_01v8", "2", 1 ]
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
            "w_0_124#",
            [
              [ "sky130_fd_pr__pfet_01v8", "4", 1 ]
            ]
          ],
          [
            "vdd",
            [
              [ "sky130_fd_pr__pfet_01v8", "1|3", 1 ]
            ]
          ]
        ]
      ]
   ]

extract_and_compare_deep_general(badnets)