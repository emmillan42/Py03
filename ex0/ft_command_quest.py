import sys

print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")

if len(sys.argv) == 1:
    print("No arguments provided!")
else:
    arguments = sys.argv[1:]
    print(f"Arguments received: {len(arguments)}")

    argument_number = 1
    for argument in arguments:
        print(f"Argument {argument_number}: {argument}")
        argument_number += 1

print(f"Total arguments: {len(sys.argv)}")
