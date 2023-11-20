# Traveling Salesman

The NP-hard problem is about a salesman who wants to visit all locations on a map traveling the shortest way. Many hard problems can be reduced to/from the TSP.

## Parameters

- $N=$ nodes/cities in the network.
- $K=$ the set of all links/arcs in the network
- $c_k=$ cost/distance in link $k$.

## Decision Variables

$x_k=1$ if $k$ is included in the TSP tour and $0$ otherwise.

## Objective Function

max $\sum_k x_kc_k\quad\forall k\in K$

## Constraints

We introduce two variables:

$L_j=$ set of all links connecting node $j$ in the network $N$

$B(S)=$ the set of all links between the cities in the subset $S$

1. $\sum_{k\in L_j}x_k=2\quad\forall j\in N$ (in-/out-flow)

2. $\sum_{k\in B(S)}x_k\leq|S|-1\quad\forall S\subset N$

## Explaination for the Constraints

1. The salesman has to visit $n$ cities and can only visit each city **once**. With the first constraint we're making sure we choose arcs such that there is a link in to and out from city $j$.

2. The second constraint is the subtour elimination. What this constraint basically is saying is: look at the set of links $B(S)$ for every subset $S$ in the network $N$. For every subset, the sum of links cannot exceed $|S|-1$, i.e. the number of cities in $S$. This ensures no subtours/cycles in the TSP tour.
