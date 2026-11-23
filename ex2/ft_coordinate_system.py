import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinates = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        values = coordinates.split(",")

        try:
            x, y, z = values
        except ValueError:
            print("Invalid syntax")
            continue

        position_values: list[float] = []

        for value in (x, y, z):
            try:
                position_values += [float(value.strip())]
            except ValueError as error:
                print(
                    f"Error on parameter '{value.strip()}': {error}"
                )
                break
        else:
            return (
                position_values[0],
                position_values[1],
                position_values[2]
            )


def main() -> None:
    print("=== Game Coordinate System ===")
    print()

    print("Get a first set of coordinates")
    position1 = get_player_pos()

    print(f"Got a first tuple: {position1}")

    x1, y1, z1 = position1
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    distance_center = math.sqrt(
        x1 ** 2 + y1 ** 2 + z1 ** 2
    )
    distance_center = round(distance_center, 4)

    print(f"Distance to center: {distance_center}")
    print()

    print("Get a second set of coordinates")
    position2 = get_player_pos()

    distance = math.sqrt(
        (position2[0] - position1[0]) ** 2
        + (position2[1] - position1[1]) ** 2
        + (position2[2] - position1[2]) ** 2
    )
    distance = round(distance, 4)

    print(f"Distance between the 2 sets of coordinates: {distance}")


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print("\nInput closed, exiting.")
