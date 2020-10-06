'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    zeros =[] 
    non_zero =[]
    for i in range(0, len(arr)):
        if arr[i]== 0:
            zeros.append(arr[i])
        else:
            non_zero.append(arr[i])
    return zeros + non_zero
    
if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")