import random
import os

NMAX = 20


def generate_graph(n, density):
    """
    Generates an undirected graph with n vertices and given density.
    Density is a value between 0 and 1.
    """

    max_edges = n * (n - 1) // 2
    target_edges = int(density * max_edges)

    edges = []
    used = set()

    while len(edges) < target_edges:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)

        if u == v:
            continue

        if u > v:
            u, v = v, u

        if (u, v) in used:
            continue

        used.add((u, v))
        edges.append((u, v))

    return edges


def write_test(filename, n, edges):
    """
    Writes the graph to a file using the required input format.
    """

    with open(filename, "w") as f:
        f.write(str(n) + " " + str(len(edges)) + "\n")

        for u, v in edges:
            f.write(str(u) + " " + str(v) + "\n")


def main():
    random.seed(42)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, "..", "tests")

    if not os.path.exists(tests_dir):
        os.mkdir(tests_dir)

    test_id = 1

    small_sizes = [2, 3]
    small_densities = [0.0, 0.3, 0.6, 1.0]

    for n in small_sizes:
        for density in small_densities:
            edges = generate_graph(n, density)
            filename = os.path.join(
                tests_dir, "test_" + str(test_id).zfill(2) + ".in"
            )
            write_test(filename, n, edges)
            test_id += 1

    medium_sizes = [5, 6, 7]
    medium_densities = [0.2, 0.5, 0.8]

    for n in medium_sizes:
        for density in medium_densities:
            edges = generate_graph(n, density)
            filename = os.path.join(
                tests_dir, "test_" + str(test_id).zfill(2) + ".in"
            )
            write_test(filename, n, edges)
            test_id += 1

    sizes = [4, 8, 10, 12, 15, 18, 20]
    densities = [0.2, 0.4, 0.6, 0.8]

    for n in sizes:
        for density in densities:
            edges = generate_graph(n, density)
            filename = os.path.join(
                tests_dir, "test_" + str(test_id).zfill(2) + ".in"
            )
            write_test(filename, n, edges)
            test_id += 1


if __name__ == "__main__":
    main()
