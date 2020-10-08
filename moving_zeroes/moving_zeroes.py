'''
Input: a List of integers
Returns: a List of integers
'''
# def moving_zeroes(arr):
#     # Your code here
#     zeros =[] 
#     non_zero =[]
#     for i in range(0, len(arr)):
#         if arr[i]== 0:
#             zeros.append(arr[i])
#         else:
#             non_zero.append(arr[i])
#     return zeros + non_zero

def moving_zeroes(arr):
    for i in arr:
        if i == 0:
            arr.remove(i)
            arr.append(i)
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")