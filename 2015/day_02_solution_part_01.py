def read_input(file_path: str) -> list[str]:
    '''Load dimensions'''
    with open(file_path) as f:
        dimensions = [line.rstrip() for line in f]
    return dimensions


def find_total_sa(dimensions: list[str]) -> int:
    '''Find total square feet of wrapping paper needed'''
    total_sa = 0
    for d in dimensions:
        l, w, h = d.split("x")
        l, w, h = int(l), int(w), int(h)
        lw, wh, hl = l * w, w * h, h * l
        shortest_side = min((lw, wh, hl))
        total_sa += 2 * (lw + wh + hl) + shortest_side
    return total_sa


def main() -> None:
    file_path = "./day_02_input.txt"
    dimensions = read_input(file_path)
    total_sa = find_total_sa(dimensions)
    print(f"total square feet of wrapping paper = {total_sa}")


if __name__ == "__main__":
    main()
