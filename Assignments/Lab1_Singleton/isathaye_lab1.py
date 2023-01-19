'''
1. The list is ordered and ascending
2. THe list has 2k + 1 elements
3. k of the numbers in the list appear twice
4. 1 number is unique
5. Find the unique number
'''

import sys

def read_file(filename):
    f = open(filename, "r")
    L = []
    for line in f:
        L.append(int(line))
    f.close()
    return L

def find_unique(L, min, max):
    # Base case
    if min == max:
        return L[min]
    # Find the middle element
    mid = (min + max) // 2
    # Check if the middle element is unique
    if L[mid] != L[mid - 1] and L[mid] != L[mid + 1]:
        return L[mid]
    if L[mid] == L[mid + 1]:
        return find_unique(L, min, mid - 1)
    else:
        return find_unique(L, mid + 1, max)
    

if __name__ == "__main__":
    filename = sys.argv[1]
    L = read_file(filename)
    print(L)
    print(find_unique(L, 0, len(L) - 1))


'''
if mid % 2 == 0:
        if L[mid] == L[mid - 1]:
            return find_unique(L, min, mid - 2)
        else:
            return find_unique(L, mid + 2, max)
    else:
        if L[mid] == L[mid - 1]:
            return find_unique(L, mid + 1, max)
        else:
            return find_unique(L, min, mid - 1)
'''