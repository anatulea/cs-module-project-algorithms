'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# def sliding_window_max(nums, k):
#     # Your code here
#     result =[]
#     for i in range(len(nums)-2):
#         # print(nums[i])
#         curr_window= [nums[i], nums[i+1], nums[i+2]]
#         # print(curr_window)
#         # print(max(curr_window))

#         result.append(max(curr_window))
#     return result


def sliding_window_max(nums, k):
    output = [0] * (len(nums) - k + 1)
    previous_max = None
    redo = True

    for i in range(len(nums) - k + 1):
        if redo:
            window = nums[i:i+k] # it starts at i and moves to the right k positions
            # print(window)
            max_val = max(window) # takes the maxim value from the window 
            output[i] = max_val
            if window[0] != max_val:
                # The max element occures somewhere else in the window
                redo = False
            # We must update max here because the previous max value will be left at the next iteration
            previous_max = max_val
        else:
            # Only compare the latest value
            previous_max = max(previous_max, nums[i+k-1])
            if nums[i] == previous_max:
                redo = True

            output[i] = previous_max

    return output
# def sliding_window_max(nums, k):	
#     max_list = []
#     i = 0
#     while i + k <= len(nums) + i:
#         window = nums[i:k]
#         max_list.append(max(window))
#         i += 1
#         k += 1
#     return max_list




if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
