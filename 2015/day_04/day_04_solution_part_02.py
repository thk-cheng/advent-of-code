import hashlib


def read_input(file_path: str) -> str:
    '''Load input string'''
    with open(file_path) as f:
        input_string = f.read().rstrip()
    return input_string


def md5_smallest(input_string: str, no_of_zeros: int) -> int:
    number = 1
    while True:
        hash_input = bytes(f"{input_string}{number}", "utf-8")
        md5_hash = hashlib.md5(hash_input).hexdigest()
        if md5_hash[:no_of_zeros] == "0" * no_of_zeros:
            break
        else:
            number += 1
    return number


def main() -> None:
    file_path = "./day_04_input.txt"
    input_string = read_input(file_path)
    no_of_zeros = 6
    smallest_number = md5_smallest(input_string, no_of_zeros)
    print(f"Smallest number = {smallest_number}")


if __name__ == "__main__":
    main()
