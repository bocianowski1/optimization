from n_queens.solve import n_queens
from knapsack.solve import knapsack
from traveling_salesman.solve import traveling_salesman

def main():
    print("\nN-Queens Problem")
    n_queens(N=8)

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

    print("\nTraveling Salesman Problem")
    traveling_salesman()

if __name__ == "__main__":
    main()