# Capstone W.S.N. project : Algorithm 2
# by Vaibhav Srivastva
# 05-APR-2026


import random
import os

def main():
    # setting up a mock network (G(SN), Omega)
    num_nodes = 10
    network_neighbours = {}
    weights = {}    # epsilons
    print("Initialising mock W.S.N. environment...")

    # generating random neighbours and weights
    for i in range(1, num_nodes + 1):
        # assign 1 to 3 random neighbours to each node (excluding itself)
        possible_neighbours = [n for n in range(1, num_nodes + 1) if n != 1]
        network_neighbours[i] = random.sample(possible_neighbours, k = random.randint(1, 3))
        # assign random data load weights between 10 and 100
        weights[i] = random.randint(10, 100)

    # selection of forwarding sensor nodes
    forwarding_nodes = {}
    for i in network_neighbours:
        neighbours = network_neighbours[i]  # set of neighbouring nodes

        # if a node happens to not have any neighbours, it can not forward data
        if not(neighbours):
            forwarding_nodes[i] = None
            continue

        # find max. of epsilons (the neighbours with the maximum weight)
        max_neighbour = max(neighbours, key = lambda n : weights[n])
        max_neighbour_weight = weights[max_neighbour]

        # CASE 1. node i's weight is less than its max. neighbour's weight
        if weights[i] < max_neighbour_weight:
            # forward to the neighbour with the maximum weight
            forwarding_nodes[i] = max_neighbour

        # CASE 2. node i's weight is greater than or equal to its max neighbour's weight
        else:
            # forward to the neighbour's neighbour (ne_k) with maximum weight
            neighbours_of_max = network_neighbours[max_neighbour]
            if neighbours_of_max:
                k = max(neighbours_of_max, key = lambda n : weights[n])
                forwarding_nodes[i] = k
            else :
                # FALLBACK (if the neighbour has no further connections)
                forwarding_nodes[i] = max_neighbour

    # outputting to a file
    output_filename = "algo_2.txt"

    with open(output_filename, 'w') as f:
        f.write("Algorithm 2 : Selection of Forwarding Sensor Nodes\n")
        f.write ("-" * 50 + "\n")

        f.write("Node Data Load Weights (epsilon) :\n")
        for node, weight, in weights.items():
            f.write(f"\tNode {node} : {weight}\n")
        
        f.write("\nNetwork Connections (NE) :\n")
        for node, neighbours in network_neighbours.items():
            f.write(f"\tNode {node} is connected to -> Node(s) {neighbours}\n")
        
        f.write("\nSelected Forwarding Nodes (FN) :\n")
        for node, fn in forwarding_nodes.items():
            f.write(f"\tNode {node} forwards data to -> Node {fn}\n")
    
    print(f"\nSuccess! Algorithm 2 executed.")
    print(f"Results written to : {os.path.abspath(output_filename)}")

if __name__ == "__main__":
    main()