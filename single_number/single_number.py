'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# def single_number(arr):
#     # Your code here
#     solution = arr[0]
#     for i in range(1, len(arr)):
#         solution = solution ^ arr[i]
#     return solution


# O(n^2)
# def single_number(arr): 
#     for element in arr: # O(n)
#         if arr.count(element) == 1: # O(n)
#             return element


# O(n)
def single_number(arr): 
    # sets are useful for when we need the uniqeness property 
    s = set()
    for num in arr: # O(n)
        if num in s: # O(1)
            s.remove(num) # O(1)
        else:
            s.add(num) # O(1)
    # at this point the only element in the set is our odd element
    # to get the element we need to transform the set to a list and grab the element
    return list(s)[0] # O(1)

# O (n^2)
# def single_number(arr): 
#     # sets are useful for when we need the uniqeness property 
#     s = []
#     for num in arr: # O(n)
#         if num in s: # O(n)
#             s.remove(num) # O(1)
#         else:
#             s.append(num) # O(1)
#     # at this point the only element in the set is our odd element
#     # to get the element we need to transform the set to a list and grab the element
#     return s.pop() # O(1)

            
if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 9, 0, 0,99]

    print(f"The odd-number-out is {single_number(arr)}")