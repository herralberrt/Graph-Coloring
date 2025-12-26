import csv
import os
import matplotlib.pyplot as plt
from collections import defaultdict


ALGO_STYLE = {
    "backtracking": {
        "color": "tab:blue",
        "linestyle": "-",
        "marker": "o"
    },
    "dsatur": {
        "color": "gold",
        "linestyle": "--",
        "marker": "s"
    },
    "rlf": {
        "color": "tab:green",
        "linestyle": "-.",
        "marker": "^"
    }
}


def read_results(csv_file):
    """
    Reads results.csv and groups rows by algorithm.
    """
    data = defaultdict(list)

    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            alg = row["algorithm"]

            data[alg].append({
                "vertices": int(row["vertices"]),
                "edges": int(row["edges"]),
                "colors": int(row["colors"]),
                "time": float(row["time_seconds"])
            })

    return data


def average_by_key(rows, key_x, key_y):
    """
    Computes average of key_y grouped by key_x.
    Returns sorted lists of x values and averaged y values.
    """
    grouped = defaultdict(list)

    for r in rows:
        grouped[r[key_x]].append(r[key_y])

    x_vals = []
    y_vals = []

    for x in sorted(grouped.keys()):
        avg = sum(grouped[x]) / len(grouped[x])
        x_vals.append(x)
        y_vals.append(avg)

    return x_vals, y_vals


def plot_time_vs_vertices(data, output_dir):
    """
    Comparative plot: execution time vs number of vertices.
    """
    plt.figure()

    for alg, rows in data.items():
        style = ALGO_STYLE[alg]
        x, y = average_by_key(rows, "vertices", "time")

        plt.plot(
            x, y,
            label=alg,
            color=style["color"],
            linestyle=style["linestyle"],
            marker=style["marker"]
        )

    plt.xlabel("Number of vertices")
    plt.ylabel("Execution time (seconds)")
    plt.title("Execution time vs Graph size")
    plt.legend()
    plt.grid(True)

    plt.savefig(os.path.join(output_dir, "time_vs_vertices.png"))
    plt.close()


def plot_colors_vs_density(data, output_dir):
    """
    Comparative plot: number of colors vs graph density.
    """
    plt.figure()

    for alg, rows in data.items():
        style = ALGO_STYLE[alg]
        grouped = defaultdict(list)

        for r in rows:
            n = r["vertices"]
            m = r["edges"]
            max_edges = n * (n - 1) / 2

            if max_edges == 0:
                continue

            density = round(m / max_edges, 2)
            grouped[density].append(r["colors"])

        x_vals = []
        y_vals = []

        for d in sorted(grouped.keys()):
            avg = sum(grouped[d]) / len(grouped[d])
            x_vals.append(d)
            y_vals.append(avg)

        plt.plot(
            x_vals, y_vals,
            label=alg,
            color=style["color"],
            linestyle=style["linestyle"],
            marker=style["marker"]
        )

    plt.xlabel("Graph density")
    plt.ylabel("Number of colors")
    plt.title("Colors used vs Graph density")
    plt.legend()
    plt.grid(True)

    plt.savefig(os.path.join(output_dir, "colors_vs_density.png"))
    plt.close()


def plot_per_algorithm(data, output_dir):
    """
    Generates individual plots for each algorithm.
    """
    per_alg_dir = os.path.join(output_dir, "per_algorithm")
    if not os.path.exists(per_alg_dir):
        os.mkdir(per_alg_dir)

    for alg, rows in data.items():
        style = ALGO_STYLE[alg]

        x_time, y_time = average_by_key(rows, "vertices", "time")

        plt.figure()
        plt.plot(
            x_time, y_time,
            color=style["color"],
            linestyle=style["linestyle"],
            marker=style["marker"]
        )
        plt.xlabel("Number of vertices")
        plt.ylabel("Execution time (seconds)")
        plt.title(f"{alg} – Execution time vs Graph size")
        plt.grid(True)

        plt.savefig(os.path.join(per_alg_dir, f"{alg}_time.png"))
        plt.close()

        grouped = defaultdict(list)

        for r in rows:
            n = r["vertices"]
            m = r["edges"]
            max_edges = n * (n - 1) / 2

            if max_edges == 0:
                continue

            density = round(m / max_edges, 2)
            grouped[density].append(r["colors"])

        x_vals = []
        y_vals = []

        for d in sorted(grouped.keys()):
            avg = sum(grouped[d]) / len(grouped[d])
            x_vals.append(d)
            y_vals.append(avg)

        plt.figure()
        plt.plot(
            x_vals, y_vals,
            color=style["color"],
            linestyle=style["linestyle"],
            marker=style["marker"]
        )
        plt.xlabel("Graph density")
        plt.ylabel("Number of colors")
        plt.title(f"{alg} – Colors used vs Graph density")
        plt.grid(True)

        plt.savefig(os.path.join(per_alg_dir, f"{alg}_colors.png"))
        plt.close()


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(base_dir, "..", "results.csv")
    plots_dir = os.path.join(base_dir, "..", "plots")

    if not os.path.exists(plots_dir):
        os.mkdir(plots_dir)

    data = read_results(csv_file)

    plot_time_vs_vertices(data, plots_dir)
    plot_colors_vs_density(data, plots_dir)
    plot_per_algorithm(data, plots_dir)

    print("Plots generated in:", plots_dir)


if __name__ == "__main__":
    main()
