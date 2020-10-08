"""
Given a sorted array, find the smallest number that is missing from the array. 
Examples 
Input: [0, 1, 2, 6, 9]
Output: 3
Input: [4, 5, 10, 11]
Output: 0
Input: [0, 1, 2, 3]
Output: 4
Input: [0, 1, 2, 3, 4, 5, 6, 7, 10]
Output: 8
"""
# --------- Method one --------
# def  find_smallest_missing(arr):
#     if arr[0] != 0:
#         return 0
#     for i in range(len(arr)-1):
#         if arr[i+1] != arr[i]+1:
#             return arr[i]+1
#     return arr[-1]+1


# --------- Method two --------
# would be the first element that does not match it's index
# arr          [0  1  2  6  7  9  11  12]
#               ^  ^  ^  ^  ^  ^  ^  ^
# index of arr [0  1  2  3  4  5  6  7 ]


#  Version 1
# def  find_smallest_missing(arr):
#     if arr[0] != 0:
#         return 0
#     # add another check to see if arr[-1] == len(arr)-1
#     if arr[-1] == len(arr)-1:
#         # no elements are missing
#         return len(arr)

#     for i in range(len(arr)-1):
#         if arr[i+1] != arr[i]+1:
#             return arr[i]+1
#     return arr[-1]+1


#  Version 2
# O(n) traversal through the entire array
# we don't take advantage of the fact that the array is sorted
# improved runtime to O(log n)
#if arr is not sorted will get a O(n log n)
def find_smallest_missing(arr):
    if arr[0] != 0:
        return 0
    # add another check to see if arr[-1] == len(arr)-1
    if arr[-1] == len(arr)-1:
        # no elements are missing
        return len(arr)

    start = 0
    end = len(arr)-1

    while start < end:
        mid = start = (start+end)//2
        if arr[mid] == mid:
            # toss out the left side
            # don't include the mid point since we know it matches it's index
            start = mid + 1
        else:
            # toss out the right 
            # but keep the midpoint, since we can't rule out that it might be the smallest missing
            end = mid
    # we've narrowed it down to one number
    # at this point start == end , so return either
    return end


A1 = [0, 1, 2, 6, 9, 11, 15]
A2 = [1, 2, 3, 4, 6, 9, 15]
A3 = [0, 1, 2, 3, 4, 5, 6]

print(find_smallest_missing(A1))
print(find_smallest_missing(A2))
print(find_smallest_missing(A3))
