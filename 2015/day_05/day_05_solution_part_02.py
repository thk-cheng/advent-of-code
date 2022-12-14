def read_input(file_path: str) -> list[str]:
    '''Load strings'''
    with open(file_path) as f:
        strings = [line.rstrip() for line in f]
    return strings


def count_nice(strings: list[str]) -> int:
    '''Count the number of strings that are nice'''
    nice_cnt = 0
    for s in strings:
        # Initialize counter for the requirements
        pair_cnt = 0
        repeat_cnt = 0

        # Loop over each letter in each string
        for idx, l in enumerate(s):
            # Check pair condition
            if idx < len(s) - 3:
                target = s[idx:idx + 2]
                # Loop over all the pairwise letters after the target, see if any of them match
                for j in range(idx + 2, len(s) - 1):
                    if target == s[j:j + 2]:
                        pair_cnt += 1

            # Check repeat condition
            if idx < len(s) - 2:
                if l == s[idx + 2]:
                    repeat_cnt += 1

        # Increment the counter for nice string if both conditions are met
        if (pair_cnt >= 1) and (repeat_cnt >=1):
            nice_cnt += 1
    return nice_cnt


def main() -> None:
    file_path = "./day_05_input.txt"
    strings = read_input(file_path)
    nice_cnt = count_nice(strings)
    print(f"Number of nice strings = {nice_cnt}")


if __name__ == "__main__":
    main()
