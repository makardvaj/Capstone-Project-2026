# Algorithm 3: Uniform Packet Generation (Correct & Minimal)

import math

def get_mcV():
    return [
        math.pi, math.e, 1.6180339887, 2.5029078750,
        1.3247179572, 4.6692016091, 2.6854520010, 1.9021605831
    ]


def algorithm3(n, t, P1, P2):
    mcV = get_mcV()

    # Step 1: Initialize X array (ONLY time-based as per paper)
    X = [0] * (t + 1)

    # Step 2: Initialize Y matrix
    Y = [[0 for _ in range(t)] for _ in range(n)]

    # Step 3: Initial seed
    X[0] = mcV[P2 % len(mcV)]

    # Step 4: constants
    a = mcV[int(X[0] % len(mcV))]
    c = mcV[int((X[0] + len(mcV)//2) % len(mcV))]

    if a == c:
        c = mcV[(int(X[0]) + 1) % len(mcV)]

    lam = 1

    # Step 5: Generate values
    for i in range(n):
        for j in range(1, t + 1):

            # Generate X[j % t]
            X[j % t] = (a * (a * X[j - 1] + c)) % (P2 - P1) + P1

            # Compute Y[i][j]
            r = X[j % t] / P2
            r = min(max(r, 1e-10), 1 - 1e-10)

            Y[i][j - 1] = (-1 / lam) * math.log(1 - r)

    return Y, a, c


def save_dataset(Y):
    with open("algo3_dataset.txt", "w") as f:
        f.write("Node\t" + "\t".join([f"t{i+1}" for i in range(len(Y[0]))]) + "\n")
        for i, row in enumerate(Y):
            f.write(f"{i+1}\t" + "\t".join([str(round(val, 4)) for val in row]) + "\n")


# -------- MAIN --------
if __name__ == "__main__":

    n = 50   # number of nodes
    t = 5    # time slots
    P1 = 2   # min packet
    P2 = 10  # max packet

    Y, a, c = algorithm3(n, t, P1, P2)

    print("=== Algorithm 3 Output ===")
    print("a =", a)
    print("c =", c)

    print("\nFirst 5 Nodes:")
    for i in range(5):
        print(f"Node {i+1}: {[round(val,2) for val in Y[i]]}")

    save_dataset(Y)

    print("\nDataset saved as 'algo3_dataset.txt'")