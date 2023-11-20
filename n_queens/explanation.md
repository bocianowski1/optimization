# N-Queens

The goal is to maximize the number of queens on an $N\times N$ chessboard. This means there can only be one queen on each row and each column. Additionally, there must be constraints that make sure no two queens share a diagonal.

## Parameters

- $N\in\Z^+ =$ number of columns and rows.
- $R=\{1,...,N\}$
- $C=\{1,...,N\}$

## Decision Variables

$x_{ij}=1$ if there is a queen at $(i,j)$ and $0$ otherwise.

## Objective Function

max $\sum_{ij}x_{ij}$ for $i\in R$ and $j\in C$

## Constraints

1. $\sum_i x_{ij}=1$ for $i\in R$ (rows)

2. $\sum_j x_{ij}=1$ for $j\in C$ (columns)

3. $\sum_{i+j=k}x_{ij}\leq1$ for $k\in\{2,...,2N\}$ (diagonal)

4. $\sum_{i-j=k}x_{ij}\leq1$ for $k\in\{-(N-1),...,(N-1)\}$ (diagonal)

## Explaination for the Constraints

The first two constraints are trivial: there must be $1$ queen at each row and column. There are two constraints making sure no two queens share a diagonal:

### Top-Left to Bottom-Right

$\sum_{i+j=k}x_{ij}\leq1$ for $k\in\{2,...,2N\}$

The first iteration, when $i=j=1$ and $k=i+j=2$, there is only on spot on the board a queen can be placed: $(1,1)$.

The second iteration, when $k=i+j=3$, there are two possible locations: $(1,2)$ and $(2,1)$.

The third iteration, when $k=i+j=4$, there are three possible locations: $(1,3)$, $(2,2)$ and $(3,1)$.

When the board is $8\times8$, $k$ goes up to $16$, the only spot is the bottom-right corner: $(8,8)$

### Top-Right to Bottom-Left

$\sum_{i-j=k}x_{ij}\leq1$ for $k\in\{-(N-1),...,(N-1)\}$

Let's assume $N$ is $8$.

The first iteration, when $k=i-j=-(N-1)=-7$, there is only on spot on the board a queen can be placed - the top-right corner: $(1,8)$. This is because there is only one possible combination: $1-8=-7$.

The next iterations follow the same pattern as the other diagonal constraint: The next iteration has two possible coordinates: $(1,7)$ and $(2,8)$.
