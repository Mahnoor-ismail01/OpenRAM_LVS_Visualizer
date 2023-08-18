def parse_netlist(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    connection_counts = {}
    in_subckt = False
    ports = []  # to store the pins from .subckt

    for line in lines:
        line = line.strip()

        if '.ends' in line:
            in_subckt = False

        if in_subckt:
            tokens = line.split()
            for token in tokens:
                # Only count the pins that are in the ports list
                if token in ports:
                    if token not in connection_counts:
                        connection_counts[token] = 1
                    else:
                        connection_counts[token] += 1

        if '.subckt' in line:
            in_subckt = True
            ports = line.split()[2:]  # ports are listed after .subckt and before component instances
            for port in ports:
                # Initialize count for each port, counting its occurrence in the .subckt line as a connection
                if port not in connection_counts:
                    connection_counts[port] = 1

    return connection_counts





