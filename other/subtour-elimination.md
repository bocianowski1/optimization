# Subtour Elimination

There are a few ways to eliminate a subtour.

## Dantzig, Fulkerson & Johnson (DFJ)

$\sum_{i\in N}\sum_{j\in S}x_{ij}\leq |S|-1,\quad\forall S\subset N, 2\leq|S|\leq|N|-1$

Alternatively,

$\sum_{k\in B(S)}x_k\leq|S|-1\quad\forall S\subset N$

Where, $B(S)=$ the set of all links between the cities in the subset $S$

## Miller, Tucker & Zemlin (MTZ)

$u_i+1\leq u_j+|N|(1-x_{ij})$ for $i,j\geq 2\in N,i\neq j$

$u_i$ tells us if node $i$ is visited and if it is, where in the visitation sequence. This ensures that $i$ comes before $j$ in a tour, preventing a cycle.
