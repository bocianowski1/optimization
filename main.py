from n_queens.solve import n_queens
from knapsack.solve import knapsack

def main():
    print("\nN-Queens Problem")
    for n in [4, 8]:
        print(f"\nN = {n}")
        n_queens(n)

    print("\nKnapsack Problem")
    items = {
        1: {"weight": 2, "benefit": 10},
        2: {"weight": 3, "benefit": 5},
        3: {"weight": 5, "benefit": 15},
        4: {"weight": 7, "benefit": 7},
        5: {"weight": 1, "benefit": 8}
    }
    for w in [6, 12]:
        print(f"\nCapacity = {w}")
        knapsack(items, w)

if __name__ == "__main__":
    main()