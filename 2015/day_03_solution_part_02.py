def read_input(file_path: str) -> str:
    '''Load directions'''
    with open(file_path) as f:
        directions = f.read()
    return directions


def count_house_with_robo(directions: str) -> int:
    '''With Robo-Santa, count the number of houses that receive at least one present'''
    houses = {"santa": [(0, 0)], "robo": [(0, 0)]}
    for turn, d in enumerate(directions):
        mover = "santa" if turn % 2 == 0 else "robo"
        last_house = houses[mover][-1]
        if d == "^":
            new_house = (last_house[0], last_house[1] + 1)
        elif d == ">":
            new_house = (last_house[0] + 1, last_house[1])
        elif d == "v":
            new_house = (last_house[0], last_house[1] - 1)
        elif d == "<":
            new_house = (last_house[0] - 1, last_house[1])
        houses[mover].append(new_house)
    combined_houses = set(houses["santa"]) | set(houses["robo"])
    return len(combined_houses)


def main() -> None:
    file_path = "./day_03_input.txt"
    directions = read_input(file_path)
    number_of_house = count_house_with_robo(directions)
    print(f"With Robo-Santa, number of houses that receive at least one present = {number_of_house}")


if __name__ == "__main__":
    main()
