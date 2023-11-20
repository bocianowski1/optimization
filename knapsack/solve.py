import gurobipy as gp
from gurobipy import GRB


def knapsack(items, capacity):
    if capacity <= 0:
        raise ValueError("Capacity must be greater than 0.")

    # Model
    m = gp.Model()
    m.setParam("OutputFlag", 0)

    # Variables
    x = m.addVars(items, vtype=GRB.BINARY, name="x")

    # Objective function
    m.setObjective(
        gp.quicksum(items[i]["benefit"] * x[i] for i in items),
        GRB.MAXIMIZE
    )

    # Constraint
    m.addConstr(
        gp.quicksum(items[i]["weight"] * x[i] for i in items) <= capacity
    )

    # Optimize
    m.optimize()

    # Print solution (amount of each item in knapsack)
    print("Items in knapsack:")
    for i in items:
        if x[i].x > 0.5:
            print(f"\tItem {i}: {x[i].x}")

    # Print solution (total benefit)
    print(f"Total benefit: {m.objVal}")
