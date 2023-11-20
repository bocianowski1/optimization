from itertools import combinations
import gurobipy as gp
from gurobipy import GRB

from .data import cities, dist


def traveling_salesman():
    print(f"({len(cities)}) Cities:", cities)
    print(f"Number of connections (edges): {len(dist)}")

    # Model
    m = gp.Model()
    m.setParam("OutputFlag", 0)

    # Variables
    vars = m.addVars(dist.keys(), obj=dist, vtype=GRB.BINARY, name='x')

    # Constraints for symmetric TSP
    for i, j in dist.keys():
        vars[j, i] = vars[i, j]

    m.addConstrs(vars.sum(c, '*') == 2 for c in cities)

    m._vars = vars
    m.Params.lazyConstraints = 1
    m.optimize(subtour_elimination)

    solution = m.getAttr('x', vars)
    selected = gp.tuplelist((i, j) for i, j in solution.keys() if solution[i, j] > 0.5)

    tour = subtour(selected)
    print('\nOptimal tour: %s' % str(tour))
    assert len(tour) == len(cities)


def subtour_elimination(model, where):
    if where == GRB.Callback.MIPSOL:
        vals = model.cbGetSolution(model._vars)
        selected = gp.tuplelist((i, j) for i, j in model._vars.keys() if vals[i, j] > 0.5)
        tour = subtour(selected)

        if len(tour) < len(cities):
            model.cbLazy(gp.quicksum(model._vars[i, j] for i, j in combinations(tour, 2)) <= len(tour) - 1)


def subtour(edges):
    unvisited = cities[:]
    cycle = cities[:]
    while unvisited:
        curr = []
        neighbors = unvisited
        while neighbors:
            curr.append(neighbors[0])
            unvisited.remove(neighbors[0])
            neighbors = [j for _, j in edges.select(curr[-1], '*') if j in unvisited]

        if len(curr) <= len(cycle):
            cycle = curr

    return cycle
