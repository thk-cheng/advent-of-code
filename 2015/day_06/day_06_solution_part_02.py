import numpy as np


def read_input(file_path: str) -> list[str]:
    '''Load instructions'''
    with open(file_path) as f:
        instructions = [line.rstrip() for line in f]
    return instructions


def count_brightness(instructions: list[str], dim: tuple[int, int]) -> int:
    '''Count the total brightness of all lights'''
    lights = np.zeros(dim, dtype=int)
    for ins in instructions:
        ins_list = ins.split(" ")
        if ins_list[0] == "turn":
            start = [int(num) for num in ins_list[2].split(",")]
            end = [int(num) for num in ins_list[-1].split(",")]
            if ins_list[1] == "on":
                lights[start[0]:end[0]+1, start[1]:end[1]+1] += 1
            elif ins_list[1] == "off":
                lights[start[0]:end[0]+1, start[1]:end[1]+1] -= 1
                lights[lights < 0] = 0
        elif ins_list[0] == "toggle":
            start = [int(num) for num in ins_list[1].split(",")]
            end = [int(num) for num in ins_list[-1].split(",")]
            lights[start[0]:end[0]+1, start[1]:end[1]+1] += 2
    return np.sum(lights)


def main() -> None:
    file_path = "./day_06_input.txt"
    instructions = read_input(file_path)
    dimensions = (1000, 1000)
    brightness = count_brightness(instructions, dimensions)
    print(f"Total brightness = {brightness}")


if __name__ == "__main__":
    main()
