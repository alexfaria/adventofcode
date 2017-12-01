def to_int_array(input_array):
    array = []
    for x in input_array:
        array.append(int(x))

    return array

def sum_first(input_array):
    array = to_int_array(input_array)
    tam = len(array)
    total = 0

    for i, x in enumerate(array):
        if x == array[(i+1) % tam]:
            total += x
    return total

def sum_second(input_array):
    array = to_int_array(input_array)
    tam = len(array)
    half = tam/2
    total = 0

    for i, x in enumerate(array):
        if x == array[(i+half) % tam]:
            total += x
    return total

if __name__ == "__main__":
    with open("day01.txt") as f:
        inp = f.read().strip()
        print(sum_first(inp))   # 1171
        print(sum_second(inp))  # 1024

# pytest
def test_sum_first():
    assert sum_first("1122") == 3
    assert sum_first("1111") == 4
    assert sum_first("1234") == 0
    assert sum_first("91212129") == 9

def test_sum_second():
    assert sum_second("1212") == 6
    assert sum_second("1221") == 0
    assert sum_second("123425") == 4
    assert sum_second("123123") == 12
    assert sum_second("12131415") == 4
