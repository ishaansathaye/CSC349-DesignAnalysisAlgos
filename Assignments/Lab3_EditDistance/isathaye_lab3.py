import sys

def calc_edit_distance(a, b):
    # Initialize the matrix
    matrix = [[0 for x in range(len(b) + 1)] for y in range(len(a) + 1)]

    # Fill in the first row and column
    for i in range(len(a) + 1):
        matrix[i][0] = i
    for j in range(len(b) + 1):
        matrix[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]) + 1

    # Return the edit distance
    # return matrix[len(a)][len(b)]
    return matrix

if __name__ == "__main__":
    # a = sys.argv[1]
    # b = sys.argv[2]
    # a = "snowy"
    a = "exponential"
    b = "polynomial"
    matrix = calc_edit_distance(a, b)
    for row in matrix:
        print(row)