import sys

if len(sys.argv) == 1:
    print("Usage: python3 ft_inventory_system.py <item>:<quantity> ...")

print("=== Inventory System Analysis ===")

inventory: dict[str, int] = {}

for argument in sys.argv[1:]:
    try:
        item_name, quantity_str = argument.split(":")
    except ValueError:
        print(f"Error - invalid parameter '{argument}'")
        continue

    if item_name in inventory:
        print(f"Redundant item '{item_name}' - discarding")
        continue

    try:
        quantity = int(quantity_str)
    except ValueError as error:
        print(f"Quantity error for '{item_name}': {error}")
        continue

    if quantity < 0:
        print(f"Quantity error for '{item_name}': negative quantity")
        continue

    inventory[item_name] = quantity

print(f"Got inventory: {inventory}")

item_list = list(inventory.keys())
print(f"Item list: {item_list}")

total_quantity = sum(inventory.values())
print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

if total_quantity > 0:
    for item in item_list:
        percentage = round(inventory[item] / total_quantity * 100, 1)
        print(f"Item {item} represents {percentage}%")
else:
    print("Cannot calculate percentages: total quantity is 0")

if inventory:
    most_abundant_item = item_list[0]
    most_abundant_quantity = inventory[most_abundant_item]

    least_abundant_item = item_list[0]
    least_abundant_quantity = inventory[least_abundant_item]

    for item in item_list[1:]:
        quantity = inventory[item]

        if quantity > most_abundant_quantity:
            most_abundant_item = item
            most_abundant_quantity = quantity

        if quantity < least_abundant_quantity:
            least_abundant_item = item
            least_abundant_quantity = quantity

    print(
        f"Item most abundant: {most_abundant_item} "
        f"with quantity {most_abundant_quantity}"
    )
    print(
        f"Item least abundant: {least_abundant_item} "
        f"with quantity {least_abundant_quantity}"
    )
if "magic_item" not in inventory:
    inventory.update({"magic_item": 1})
print(f"Updated inventory: {inventory}")
