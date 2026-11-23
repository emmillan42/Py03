import random


achievements = [
    "Awake",
    "Beta Explorer",
    "Boss Slayer",
    "Collector Supreme",
    "Crafting Genius",
    "First Steps",
    "Grand Master of all things",
    "Hidden Path Finder",
    "It's a rich man's world",
    "Master Explorer",
    "Popular",
    "Rigorous Basterd",
    "Sharp Mind",
    "Speed Runner",
    "Strategist",
    "Survivor",
    "Treasure Hunter",
    "Unstoppable",
    "Untouchable",
    "World Savior"
]


def gen_player_achievements() -> set[str]:
    total = len(achievements)
    half = total // 2

    low = half - 1
    if low < 0:
        low = 0

    high = half + 1
    if high > total:
        high = total

    number = random.randint(low, high)
    selected = random.sample(achievements, number)
    player_achievements = set(selected)
    return player_achievements


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()

    alice = gen_player_achievements()
    print(f"Player Alice: {alice}")

    bob = gen_player_achievements()
    print(f"Player Bob: {bob}")

    charlie = gen_player_achievements()
    print(f"Player Charlie: {charlie}")

    dylan = gen_player_achievements()
    print(f"Player Dylan: {dylan}")
    print()

    all_achievements = set(achievements)
    all_distinct_achievements = (
        alice.union(bob).union(charlie).union(dylan)
    )
    print(f"All distinct achievements: {all_distinct_achievements}")
    print()

    common_achievements = (
        alice.intersection(bob).intersection(charlie).intersection(dylan)
    )
    print(f"Common achievements: {common_achievements}")
    print()

    alice_unique = alice.difference(bob.union(charlie).union(dylan))
    print(f"Only Alice has: {alice_unique}")

    bob_unique = bob.difference(alice.union(charlie).union(dylan))
    print(f"Only Bob has: {bob_unique}")

    charlie_unique = charlie.difference(alice.union(bob).union(dylan))
    print(f"Only Charlie has: {charlie_unique}")

    dylan_unique = dylan.difference(alice.union(bob).union(charlie))
    print(f"Only Dylan has: {dylan_unique}")
    print()

    alice_missing = all_achievements.difference(alice)
    print(f"Alice is missing: {alice_missing}")

    bob_missing = all_achievements.difference(bob)
    print(f"Bob is missing: {bob_missing}")

    charlie_missing = all_achievements.difference(charlie)
    print(f"Charlie is missing: {charlie_missing}")

    dylan_missing = all_achievements.difference(dylan)
    print(f"Dylan is missing: {dylan_missing}")


if __name__ == "__main__":
    main()
