import sys
import os
import time

from concorde.tsp import TSPSolver

def run_concorde(tsp_file):
    start = time.time()

    tsp_path = os.path.abspath(tsp_file)
    tsp_dir = os.path.dirname(tsp_path)
    tsp_name = os.path.splitext(os.path.basename(tsp_path))[0]
    out_file = os.path.join(tsp_dir, tsp_name + ".sol")

    solver = TSPSolver.from_tspfile(tsp_path)
    solution = solver.solve()

    end = time.time()
    execution = end - start

    with open(out_file, 'w') as f:
        f.write(f"{solution.optimal_value} {execution:.4f} ")
        f.write(" ".join(map(str, solution.tour)))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 run_concorde.py <tsp_file>")
        sys.exit(1)

    tsp_file = sys.argv[1]

    run_concorde(tsp_file)

