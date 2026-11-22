import random
import typing


players = ["alice", "bob", "charlie", "dylan"]

actions = [
    "run", "eat", "sleep", "grab", "move", "climb", "swim",
    "release", "use"
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        event = (player, action)
        yield event


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        event = random.choice(events)
        events.remove(event)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event()

    for i in range(1000):
        player, action = next(event_generator)
        print(f"Event {i}: Player {player} did action {action}")

    stored_events: list[tuple[str, str]] = []
    event_generator = gen_event()

    for _ in range(10):
        event = next(event_generator)
        stored_events.append(event)

    print(f"Built list of 10 events: {stored_events}")

    consume_ev = consume_event(stored_events)
    for event in consume_ev:
        print(f"Got event from list: {event}")
        print(f"Remains in list: {stored_events}")


if __name__ == "__main__":
    main()
