def read_input(file_path: str) -> list[list[str]]:
    '''Load strings'''
    with open(file_path) as f:
        strings = [[letter for letter in line[:-1]] for line in f]
    return strings


def count_char(strings: list[str]) -> int:
    '''Count no. of char for string literals - no. of char in memory'''
    total_code_cnt = 0
    total_mem_cnt = 0
    for s in strings:
        # the extra '+2' accounts for the open & end quotations
        total_code_cnt += (len(s) + 2)
        idx = 0
        while idx < len(s):
            if s[idx] == "\\":
                if s[idx+1] == "x":
                    total_mem_cnt += 1
                    idx += 4
                else:
                    total_mem_cnt += 1
                    idx += 2
            else:
                total_mem_cnt += 1
                idx += 1
    return total_code_cnt - total_mem_cnt


def main() -> None:
    file_path = "./day_08_input.txt"
    strings = read_input(file_path)
    no_of_char = count_char(strings)
    print(f"Answer: {no_of_char}")


if __name__ == "__main__":
    main()
