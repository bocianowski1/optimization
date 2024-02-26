# Set Partitioning

Given a set of items, you want to find a way to divide the set into subsets, meeting certain conditions. The goal is to find the optimal way to create these subsets. It can be minimization or maximization.

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
