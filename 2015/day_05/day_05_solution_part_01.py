def read_input(file_path: str) -> list[str]:
    '''Load strings'''
    with open(file_path) as f:
        strings = [line.rstrip() for line in f]
    return strings


def count_nice(strings: list[str]) -> int:
    '''Count the number of strings that are nice'''
    vowels = ("a", "e", "i", "o", "u")
    bad_strings = ("ab", "cd", "pq", "xy")
    nice_cnt = 0
    for s in strings:
        vowel_cnt = 0
        twice_cnt = 0
        contains_bad = False
        for idx, letter in enumerate(s):
            if idx != len(s) - 1:
                if s[idx:idx + 2] in bad_strings:
                    contains_bad = True
                    break
                if letter == s[idx + 1]:
                    twice_cnt += 1
            if letter in vowels:
                vowel_cnt += 1
        if (vowel_cnt >= 3) and (twice_cnt >= 1) and (not contains_bad):
            nice_cnt += 1
    return nice_cnt


def main() -> None:
    file_path = "./day_05_input.txt"
    strings = read_input(file_path)
    nice_cnt = count_nice(strings)
    print(f"Number of nice strings = {nice_cnt}")


if __name__ == "__main__":
    main()
