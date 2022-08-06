def read_input(file_path: str) -> list[str]:
    '''Load circuit instructions'''
    with open(file_path) as f:
        instructions = [line.rstrip() for line in f]
    return instructions


def is_number(string: str) -> bool:
    '''Helper function for checking whether a string can be converted into integer or not'''
    answer = True
    try:
        _ = int(string)
    except ValueError:
        answer = False
    finally:
        return answer


def find_all_elements(instructions: list[str]) -> list[tuple[list[str], str]]:
    '''Helper function for finding all elements in the circuit'''
    elements = [(line.split(" -> ")[0].split(" "), line.split(" -> ")[-1]) for line in instructions]
    elements = sorted(elements, key=lambda x: (len(x[-1]), x[-1]))
    elements = elements[1:] + [elements[0]] # Move "a" to the last
    return elements


def build_circuit(instructions: list[str], nob: int) -> dict[str, int]:
    '''Build circuit from instructions'''
    elements = find_all_elements(instructions)
    circuit = {}
    for wiring, e in elements:
        if len(wiring) == 1:
            wiring = wiring[0]
            if is_number(wiring):
                if e == "b":
                    circuit[e] = 16076
                else:
                    circuit[e] = int(wiring)
            else:
                circuit[e] = circuit[wiring]
        else:
            if "AND" in wiring:
                if is_number(wiring[0]):
                    circuit[e] = int(wiring[0]) & circuit[wiring[-1]]
                elif is_number(wiring[-1]):
                    circuit[e] = circuit[wiring[0]] & int(wiring[-1])
                else:
                    circuit[e] = circuit[wiring[0]] & circuit[wiring[-1]]
            elif "OR" in wiring:
                if is_number(wiring[0]):
                    circuit[e] = int(wiring[0]) | circuit[wiring[-1]]
                elif is_number(wiring[-1]):
                    circuit[e] = circuit[wiring[0]] | int(wiring[-1])
                else:
                    circuit[e] = circuit[wiring[0]] | circuit[wiring[-1]]
            elif "LSHIFT" in wiring:
                circuit[e] = circuit[wiring[0]] << int(wiring[-1])
            elif "RSHIFT" in wiring:
                circuit[e] = circuit[wiring[0]] >> int(wiring[-1])
            elif "NOT" in wiring:
                if is_number(wiring[-1]):
                    circuit[e] = ~int(wiring[-1])
                else:
                    circuit[e] = ~circuit[wiring[-1]]
    return circuit


def main():
    file_path = "./day_07_input.txt"
    instructions = read_input(file_path)
    nob = 16
    circuit = build_circuit(instructions, nob)
    print(f"a: {circuit['a']}")


if __name__ == "__main__":
    main()
