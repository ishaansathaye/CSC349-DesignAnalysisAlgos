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
    L = [int(x) for x in f]
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
    if mid % 2 == 0: # if even number of elements 
        if L[mid] == L[mid - 1]: # mid element same as previous
            return find_unique(L, min, mid - 2) # in the left half
        else: # mid element same as next
            return find_unique(L, mid + 2, max) # in the right half
    else: # if odd number of elements from 
        if L[mid] == L[mid - 1]: 
            return find_unique(L, mid + 1, max) # duplicate to the left then look right
        else:
            return find_unique(L, min, mid - 1) # duplicate to the right then look left

if __name__ == "__main__":
    filename = sys.argv[1]
    L = read_file(filename)
    print(find_unique(L, 0, len(L) - 1))
