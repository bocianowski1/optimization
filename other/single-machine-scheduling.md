# Single Machine Scheduling

A set of tasks / jobs needs to be processed on a single machine one at the time. An operation cannot be interrupted before it is complete. For every task $i$ a release date and a duration are provided.

## Sets

$J=$ set of jobs

$R=$ set of ranks, i.e. in which rank $r$ (position / order) is a job complete?

## Parameters

$S_r$ the start time for the job at position $r$ and must be at least as great as the release date $R_j$.

$D_j$ is the due date for job $j$.

## Decision Variables

$x_{jr}=1$ if job $j$ is at position $r$ and $0$ otherwise. For $j\in J$ and $r\in\set{1,...,NJ}$

## Minimizing Makespan

Total completion time of schedule.

min $S_{NJ}+\sum_{j\in J}D_jx_{j,NJ}$

## Constraints

1. $\sum_{j\in J}x_{jr}=1\quad\forall r\in R$

2. $\sum_{r\in R}x_{jr}=1\quad\forall j\in J$

3. $S_r\geq\sum_{j\in J}R_jx_{jr}\quad\forall r\in R$

4. $S_{r+1}\geq S_r+\sum_{j\in J}D_jx_{jr}\quad\forall r=1,...,NJ-1$

5. $x_{jr}\in\set{0,1}\quad\forall j\in J,r\in R$

6. $S_r\geq0\quad\forall r\in R$

## Explanation for the Constraints

The first two constriants means each job and each rank has exactly one of the other paired to it, i.e. no two jobs can share a rank in the scheduling.

The third constraint means that the start date for the job at rank $r$ cannot begin before the release date of job $j$.

The fourth constraint let's us know that a job cannot start before the preceeding job is finished.
