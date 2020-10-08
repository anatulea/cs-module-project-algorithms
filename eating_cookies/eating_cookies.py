'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
#     # if n == 0:
#     #     return 1
#     # if n == 1:
#     #     return 1
#     # if n == 2:
#     #     return 2
#     solutions = {0:1, 1:1, 2:2}
#     for i in range(3, n+1):
#         solutions[i] = solutions[i-1]+ solutions[i-2]+solutions[i-3]
#     return solutions[n]
# Your code here

# Recursive --- O(n^3) --very slow
# def eating_cookies(n):
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1
#     return eating_cookies(n-1) + eating_cookies(n-2)+eating_cookies(n-3)

# BEST VERSION
# use chache
def eating_cookies(n, cache=None):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    # check the cache and check if the anwser is stored there
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            # init an empty cache
            # setting all the i keys to zero for the range (n+1)
            cache = {i: 0 for i in range(n+1)}  # dictionary comprehension
        # store answers in our cache
        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache)+eating_cookies(n-3, cache)
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 100

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
