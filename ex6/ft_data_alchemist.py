import random


players = [
    "Alice", "bob", "Charlie", "dylan",
    "Emma", "Gregory", "john", "kevin", "Liam"
]

MIN_SCORE = 0
MAX_SCORE = 1000


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()

    print(f"Initial list of players: {players}")

    capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized}")

    capitalized_only = [n for n in players if n == n.capitalize()]
    print(f"New list of capitalized names only: {capitalized_only}")
    print()

    scores = {n: random.randint(MIN_SCORE, MAX_SCORE) for n in capitalized}
    print(f"Score dict: {scores}")

    if len(scores) == 0:
        print("No players: the average cannot be computed.")
        return

    average = sum([scores[n] for n in scores]) / len(scores)
    print(f"Score average is {round(average, 2)}")

    high_scores = {n: scores[n] for n in scores if scores[n] > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
