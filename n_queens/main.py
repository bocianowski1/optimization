import numpy as np
import gurobipy as gp
from gurobipy import GRB

def n_queens(N = 8, hide_output = True, show_board = True) -> np.ndarray:
    rows = np.arange(1, N+1)
    cols = np.arange(1, N+1)

    if N < 4:
        raise ValueError("N must be greater than or equal to 4.")

    # Model
    m = gp.Model()

    if hide_output:
        m.setParam("OutputFlag", 0)

    x = m.addVars(rows, cols, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(
        gp.quicksum(x[i, j] for i in rows for j in cols)
    )

    # Constraints
    m.addConstrs(
        (
            gp.quicksum(
                x[i, j] for i in rows
            ) == 1 for j in cols
        ), name="rows"
    )

    m.addConstrs(
        (
            gp.quicksum(
                x[i, j] for j in cols
            ) == 1 for i in rows
        ), name="columns"
    )

    m.addConstrs(
        (
            gp.quicksum(
                x[i, j] for i in rows for j in cols if i+j == k
            ) <= 1 for k in np.arange(2, 2*N+1)
        ), name="diagonals1"
    )

    m.addConstrs(
        (
            gp.quicksum(
                x[i, j] for i in rows for j in cols if i-j == k
            ) <= 1 for k in np.arange(-N+1, N)
        ), name="diagonals2"
    )

    # Optimize
    m.optimize()

    if show_board:
        print_chessboard(rows, cols, x)

    return np.array([
        [x[i, j].x for j in cols] for i in rows
    ])


def print_chessboard(rows: np.ndarray, cols: np.ndarray, x: gp.tupledict) -> None:
    for i in rows:
        for j in cols:
            if x[i, j].x > 0.5:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        for j in cols:
            if x[i, j].x > 0.5:
                print(f"  {i, j}", end=" ")
        print()
    
    