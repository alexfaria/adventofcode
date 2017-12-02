def matrix_from_input(filename):
    with open(filename) as f:
        # inp = f.readline()
        matrix = [ map(int, line.split('\t')) for line in f ]
    return matrix

def checksum_first(matrix):
    checksum = 0
    for row in matrix:
        checksum += max(row) - min(row)
    return checksum

def checksum_second(matrix):
    checksum = 0
    for row in matrix:
        for x in row:
            for j in row:
                if x != j and x % j == 0:
                    checksum += x / j
    return checksum

if __name__ == '__main__':
    matrix = matrix_from_input('day02.txt')
    print(checksum_first(matrix))
    print(checksum_second(matrix))


def test_checksum_first():
    assert checksum_first([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]) == 18

def test_checksum_second():
    assert checksum_second([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]) == 9
