# Knapsack

This is a greedy approximation algorithm where the objective is to select the best items (projects, investments) given a resource constraint (time, budget, weight). There cannot be fractions / shares of an item.

## Parameters

- $I=$ set of items.
- $p_i=$ benefit of choosing item $i$.
- $w_i=$ weight of item $i$ (amount of resource it uses).
- $b=$ capacity / max weight

## Decision Variables

$x_i=1$ if item $i$ is chosen and $0$ otherwise.

## Objective Function

max $\sum_{i\in I} p_ix_i$

## Constraints

$\sum_{i\in I} p_ix_i \leq b$ (subject to maximum weight)

$x_i=\{0,1\}$ for $i\in I$ (binary variable)

## Explaination for the Constraints

This constraint is trival and show up in many different optimization problems. What's important here, is to recognize when a new problem is similar to the knapsack problem.

In general, anytime a set of items must be selected in order to maximize (or minimize) some objective, subject to a constraint on the total capacity or resource usage.

## Example from the Lecture

- A company is considering four alternatives of investments. Each alternative requires a certain cash outflow at the present time and yields a net present value (NPV), given in the table below:

  |         | Alternative 1 | Alternative 2 | Alternative 3 | Alternative 4 |
  | ------- | ------------- | ------------- | ------------- | ------------- |
  | **NPV** | $16,000       | $22,000       | $12,000       | $8,000        |
  | $I_0$   | $5,000        | $7,000        | $4,000        | $3,000        |

- Currently, $14,000 are available for investment.
- Which alternatives should be chosen such that the total NPV is maximized?
