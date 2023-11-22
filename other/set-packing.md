# Set Packing

The goal is to maximize the total number of subsets such that the selected subsets are pairwise disjoint.

The example from the lecture depicts a situation where you are in your kitchen with different food ingredients, from which you can make different dishes (from a cookbook / collection of recipes). Each recipe requires a set of ingredients. You want to make as many dishes as possible - i.e. select the maximum number of recipes that are pairwise disjoint.

## Parameters

- $N=$ set of items.
- $C=\set{S_1,...,S_t}=$ is the collection of subsets in $N$.

## Decision Variables

$x_{j}=1$ if subset $j$ is chosen and $0$ otherwise. For $j=1,...,t$.

$a_{ij}=$ if item $i$ is in subset $S_j$ and $0$ otherwise. For $j=1,...,t$ and $i\in N$.

## Objective Function

max $\sum_{j=1}^t x_j$

## Constraints

1. $\sum_{j=1}^t a_{ij}x_j\leq1$ for $i\in N$

2. $x_j\in\set{0,1}$ for $j=1,...,t$

## Explaination for the Constraints

The constraint says that, for every item $i$, we want to see if it is present in _more than_ **one** subset, i.e. if sum over every subset is greater than $1$. $a_{ij}$ let us know ($=1$) if item $i\in S_j$.
