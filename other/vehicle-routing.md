# Vehicle Routing

<i style="text-decoration: underline">Given:</i>
A set of transportation requests and a fleet of vehicles.

<i style="text-decoration: underline">Objective:</i>
Find a plan to perform all transoportation requests with the given fleet while minimizing cost. Decide which vehicle handles which request in which order.

## Applications

| Context                | Network           | Vehicles      | Locations            | Tasks         |
| ---------------------- | ----------------- | ------------- | -------------------- | ------------- |
| Distribution logistics | Roads map         | Trucks        | Customers / stores   | Deliveries    |
| Urban waste management | Streets in a city | Cleaning cars | Streets with 2 sides | Collect waste |
| Spying activites       | Earth             | Satallites    | Space xD             | Take pictures |

## Parameters

- $G=(V,E)=$ vertices and edges / links.
- $c_{ij}=$ cost between city $i$ and city $j$.

## Decision Variables

$x_{ij}=1$ if edge $(i,j)$ is chosen and $0$ otherwise

## Objective Function

min $\sum_{ij} x_{ij}c_{ij}$ for every $i$ and $j$ in $N$

## Constraints

1. $\sum_{i\in N}x_{ij}=1\quad\forall j\in N$

2. $\sum_{j\in N}x_{ij}=1\quad\forall i\in N$

3. $\sum_{i\in N}\sum_{j\in S}x_{ij}\leq|S|-1,\quad\forall S\subset N,2\leq|S|\leq|N|-1$

4. $x_{ij}\in\set{0,1}$ for every $i$ and $j$ in $N$

## Explaination for the Constraints

Similar to the [TSP](https://github.com/bocianowski1/optimization/tree/main/traveling_salesman), the first two constraints tell us that we choose exactly one path in and out of every node. The sum over $i$ of every ingoing path into node $j$ must be equal to exactly $1$.

The third constraint eliminate subtours - a subset of cities that traps the VRP in an infinite loop. That's why the sum of $x_{ij}$ must be less than the cardinality of every subset for every node $i$ and $j$.
