
import sys

print("=== Player Score Analytics ===")

scores: list[int] = []

for argument in sys.argv[1:]:
    try:
        score = int(argument)
        scores.append(score)
    except ValueError:
        print(f"Invalid parameter: '{argument}'")

if len(scores) == 0:
    print("No scores provided. Usage: python3 "
          "ft_score_analytics.py <score1> <score2> ...")
else:
    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    lowest = min(scores)
    score_range = highest - lowest

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {highest}")
    print(f"Low score: {lowest}")
    print(f"Score range: {score_range}")
print()
