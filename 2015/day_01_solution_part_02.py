def read_input(file_path: str) -> str:
    '''Load instructions'''
    with open(file_path) as f:
        instructions = f.read()
    return instructions


def find_first_basement_position(instructions: str) -> int:
    '''Infer the floor number from the instructions'''
    floor = 0
    for pos, p in enumerate(instructions, start=1):
        if p == "(":
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            first_pos = pos
            break
    return first_pos


def main() -> None:
    file_path = "./day_01_input.txt"
    instructions = read_input(file_path)
    first_basement_position = find_first_basement_position(instructions)
    print(f"position {first_basement_position}")


if __name__ == "__main__":
    main()
