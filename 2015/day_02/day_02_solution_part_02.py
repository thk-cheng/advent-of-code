def read_input(file_path: str) -> list[str]:
    '''Load dimensions'''
    with open(file_path) as f:
        dimensions = [line.rstrip() for line in f]
    return dimensions


def find_total_ribbon(dimensions: list[str]) -> int:
    '''Find total feet of ribbon needed'''
    total_ribbon = 0
    for d in dimensions:
        d_list = sorted([int(dim) for dim in d.split("x")])
        total_ribbon += 2 * (d_list[0] + d_list[1]) + d_list[0] * d_list[1] * d_list[2]
    return total_ribbon


def main() -> None:
    file_path = "./day_02_input.txt"
    dimensions = read_input(file_path)
    total_ribbon = find_total_ribbon(dimensions)
    print(f"total feet of ribbon = {total_ribbon}")


if __name__ == "__main__":
    main()
