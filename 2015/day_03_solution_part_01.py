def read_input(file_path: str) -> str:
    '''Load directions'''
    with open(file_path) as f:
        directions = f.read()
    return directions


def count_house(directions: str) -> int:
    '''Count the number of houses that receive at least one present'''
    houses = [(0, 0)]
    for d in directions:
        last_house = houses[-1]
        if d == "^":
            new_house = (last_house[0], last_house[1] + 1)
        elif d == ">":
            new_house = (last_house[0] + 1, last_house[1])
        elif d == "v":
            new_house = (last_house[0], last_house[1] - 1)
        elif d == "<":
            new_house = (last_house[0] - 1, last_house[1])
        houses.append(new_house)
    return len(set(houses))


def main() -> None:
    file_path = "./day_03_input.txt"
    directions = read_input(file_path)
    number_of_house = count_house(directions)
    print(f"Number of houses that receive at least one present = {number_of_house}")


if __name__ == "__main__":
    main()
