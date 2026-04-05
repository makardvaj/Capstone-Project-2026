def spv(position_vector, node_ids):
    """
    Sequence Position Vector (SPV) method.
    
    Converts a continuous position vector into a discrete node ID sequence
    by sorting positions in ascending order and mapping back to node IDs.
    
    Args:
        position_vector: list of continuous position values (e.g., [2.1, 1.6, 2.5, 3.8, 0.7, 2.3, 4.0])
        node_ids: list of node IDs corresponding to each dimension (e.g., [2, 16, 25, 11, 19, 8, 20])
    
    Returns:
        discrete_sequence: list of node IDs reordered by ascending position value
    """
    # Pair each position value with its corresponding node ID
    paired = list(zip(position_vector, node_ids))
    
    # Sort by position value in ascending order
    sorted_pairs = sorted(paired, key=lambda x: x[0])
    
    # Extract the node IDs in sorted order (these are the "old index/dimension" values)
    discrete_sequence = [pair[1] for pair in sorted_pairs]
    
    return discrete_sequence


def apply_spv_to_population(population):
    """
    Apply SPV to an entire population of particles.
    
    Args:
        population: list of dicts, each with 'node_ids', 'position', 'velocity'
    
    Returns:
        population with 'spv_sequence' added to each particle
    """
    for particle in population:
        particle['spv_sequence'] = spv(particle['position'], particle['node_ids'])
    return population


# ----------------------------
# Example / Demo
# ----------------------------

if __name__ == "__main__":
    # Example from Table 2 / Table 4 in the paper

    # Particle 1
    node_ids_p1     = [2,   16,   25,  11,  19,  8,   20 ]
    position_p1     = [2.1, 1.6,  2.5, 3.8, 0.7, 2.3, 4.0]
    velocity_p1     = [1.47,-1.6, -2,  3.5, 2.7, 2.3, 1.9]

    spv_p1 = spv(position_p1, node_ids_p1)
    print("=== Particle 1 ===")
    print(f"Node IDs       : {node_ids_p1}")
    print(f"Position vector: {position_p1}")
    print(f"SPV output     : {spv_p1}")
    # Expected from Table 4: [19, 16, 2, 8, 25, 11, 20]

    print()

    # Particle 2
    node_ids_p2     = [12,  6,    11,  19,   22,   3  ]
    position_p2     = [3.1, 3.6,  1.5, 2.4,  1.78, 2.6]
    velocity_p2     = [-1.2, 1.25, 3.4, 0.14, -2.8, 1.7]

    spv_p2 = spv(position_p2, node_ids_p2)
    print("=== Particle 2 ===")
    print(f"Node IDs       : {node_ids_p2}")
    print(f"Position vector: {position_p2}")
    print(f"SPV output     : {spv_p2}")
    # Expected from Table 5: [11, 22, 19, 3, 12, 6]

    print()

    # Population-level demo
    population = [
        {'node_ids': node_ids_p1, 'position': position_p1, 'velocity': velocity_p1},
        {'node_ids': node_ids_p2, 'position': position_p2, 'velocity': velocity_p2},
    ]

    population = apply_spv_to_population(population)
    print("=== Population SPV Results ===")
    for i, particle in enumerate(population, 1):
        print(f"Particle {i} SPV sequence: {particle['spv_sequence']}")