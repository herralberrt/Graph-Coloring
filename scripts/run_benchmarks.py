import os
import subprocess
import time
import csv


def run_algorithm(executable, input_file):
    """
    Runs a given executable on an input file and measures execution time.
    Returns the number of colors and execution time.
    """

    start_time = time.perf_counter()

    with open(input_file, "r") as fin:
        process = subprocess.run(
            [executable],
            stdin=fin,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

    end_time = time.perf_counter()

    output_lines = process.stdout.strip().splitlines()

    if len(output_lines) == 0:
        colors_used = 0
    else:
        colors_used = int(output_lines[0])

    exec_time = end_time - start_time

    return colors_used, exec_time


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    tests_dir = os.path.join(base_dir, "..", "tests")
    bin_dir = os.path.join(base_dir, "..", "bin")
    output_csv = os.path.join(base_dir, "..", "results.csv")

    algorithms = {
        "backtracking": os.path.join(bin_dir, "backtracking"),
        "dsatur": os.path.join(bin_dir, "dsatur"),
        "rlf": os.path.join(bin_dir, "rlf")
    }

    test_files = sorted(
        f for f in os.listdir(tests_dir)
        if f.endswith(".in")
    )

    with open(output_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow([
            "test",
            "algorithm",
            "vertices",
            "edges",
            "colors",
            "time_seconds"
        ])

        for test in test_files:
            test_path = os.path.join(tests_dir, test)

            with open(test_path, "r") as f:
                first_line = f.readline().split()
                n = int(first_line[0])
                m = int(first_line[1])

            for alg_name, alg_exec in algorithms.items():
                colors, exec_time = run_algorithm(alg_exec, test_path)

                writer.writerow([
                    test,
                    alg_name,
                    n,
                    m,
                    colors,
                    exec_time
                ])

    print("Benchmark finished.")
    print("Results saved to:", output_csv)


if __name__ == "__main__":
    main()
