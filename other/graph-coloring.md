# Graph Coloring

This problem can be reduced onto other types of situations. Given an undirected graph, anytime no two nodes can share a color or exam period or another resource, this model can be used.

## Parameters

- $N=$ the set of nodes in the graph.
- $E=$ the set of edges in the graph.
- $K=$ the set of colors and $|K|=|N|$, i.e. there are as many colors in the set as nodes in the graph.

## Decision Variables

$x_{i,c}=1$ if node $i$ is colored with the color $c$ and $0$ otherwise.

$y_{c}=1$ if color $c$ is used and $0$ otherwise.

## Objective Function

min $\sum_i y_c\quad\forall c\in K$

## Constraints

1. $x_{i,c}+x_{j,c}\leq1$ for every edge / pair $(i,j)\in E$ and color $c\in K$

2. $\sum_{c\in K} x_{i,c}=1$ for every node $i\in N$

3. $x_{i,c}\leq y_c\quad\forall i\in N$ and $c\in K$

4. $x_{i,c}\in\set{0,1}$ for each node $i\in N$

5. $y_{c}\in\set{0,1}$ for each color $c\in K$

## Explaination for the Constraints

The first one ensures that no two neighbouring nodes share the same color. The second constraint makes sure a node is assigned exactly one color. The third one is the book-keeping constraint, i.e. it makes sure we don't use more colors than we need to. If $c$ is used, then $y_c=1$, and so $x_{i,c}$ won't get a color we've already used.
