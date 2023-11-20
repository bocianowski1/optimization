from n_queens.main import n_queens

def main():
    print("N-Queens Problem")
    for n in [4, 8, 16]:
        print(f"N = {n}")
        n_queens(n)
        print()

if __name__ == "__main__":
    main()