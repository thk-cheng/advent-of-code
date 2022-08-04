def read_input(file_path: str) -> str:
    '''Load instructions'''
    with open(file_path) as f:
        instructions = f.read()
    return instructions


def count_floor(instructions: str) -> int:
    '''Infer the floor number from the instructions'''
    floor = 0
    for p in instructions:
        if p == "(":
            floor += 1
        else:
            floor -= 1
    return floor


def main() -> None:
    file_path = "./day_01_input.txt"
    instructions = read_input(file_path)
    floor = count_floor(instructions)
    print(f"floor {floor}")


if __name__ == "__main__":
    main()
