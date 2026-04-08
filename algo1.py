# Algorithm 1: Deployment (EDGF - Final Version)

import math
import matplotlib.pyplot as plt

def get_mcV():
    """Mathematical constant vector (as per paper idea)"""
    return [
        math.pi, math.e, 1.6180339887, 2.5029078750,
        1.3247179572, 4.6692016091, 2.6854520010, 1.9021605831
    ]


def algorithm1(n, m, X0):
    mcV = get_mcV()

    X = [0] * (n + 1)
    Y = [0] * (n + 1)

    X[0] = X0
    Y[0] = X0

    # Generate constants
    a = mcV[int(X0 % len(mcV))]
    c = mcV[int((X0 + len(mcV)//2) % len(mcV))]

    # Ensure a ≠ c
    if a == c:
        c = mcV[(int(X0) + 1) % len(mcV)]

    # Generate coordinates
    for i in range(1, n + 1):
        X[i] = (a * X[i - 1] + c) % m
        Y[i] = (a * Y[i - 1] + a) % m

    return X[1:], Y[1:], a, c


def save_results(X, Y):
    with open("deployment_algo1.txt", "w") as f:
        f.write("Node\tX\tY\n")
        for i in range(len(X)):
            f.write(f"{i+1}\t{round(X[i],4)}\t{round(Y[i],4)}\n")


def plot(X, Y):
    plt.figure()
    plt.scatter(X, Y)
    plt.title("EDGF Deployment (Algorithm 1)")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()


# -------- MAIN --------
if __name__ == "__main__":
    n = 50
    m = 100
    X0 = 43

    X, Y, a, c = algorithm1(n, m, X0)

    print("a =", a)
    print("c =", c)

    print("\nFirst 5 Nodes:")
    for i in range(5):
        print(f"Node {i+1}: ({round(X[i],2)}, {round(Y[i],2)})")

    save_results(X, Y)
    plot(X, Y)