import numpy as np
import gurobipy as gp
from gurobipy import GRB

N = 8
rows = np.arange(1, N+1)
cols = np.arange(1, N+1)

# Model
m = gp.Model()

# x_{i,j} = 1 if queen is placed in cell (i,j)
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

# Print solution
print("Solution:")
for i in rows:
    for j in cols:
        if x[i, j].x > 0.5:
            print(f"({i}, {j})")