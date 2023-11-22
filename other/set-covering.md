# Set Covering

The goal is to choose items from $N$ such that _at least one_ item from each subset $S_1,...,S_t$ is chosen, while minimizing cost.

For example, if there needs to be placed fire stations in an area of neighbouring districts $(=N)$, and there has to be a fire station in a district or in a neighbouring district, we can use this problem. Instead of neighbouring districts, we could use minutes it takes to drive between districts.

## Parameters

- $N=$ set of items.
- $C=\set{S_1,...,S_t}=$ is the collection of subsets in $N$.
- $c_i=$ the cost for item $i\in N$

## Decision Variables

$x_{i}=1$ if item $i$ is chosen and $0$ otherwise.

## Objective Function

min $\sum_i x_ic_i\quad\forall i\in N$

## Constraints

1. $\sum_{i\in S_j}x_i\geq1$ for $j=1,..,t$

2. $x_i\in\set{0,1}$ for $i\in N$

## Explaination for the Constraints

The constraint says that, for every subset in $N$, we _at least_ have to choose **one** item from that subset. That way we ensure that we include an item from each subset, while minimizing cost - which was the objective.
