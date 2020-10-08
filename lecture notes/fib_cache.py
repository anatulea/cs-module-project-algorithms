# cache is going to store the subproblems for fib se we don't  have to keep re-calculating them
cache ={} # keys: n( in the input param) values: the nth fib number/ the return value from the function
def fib_cache(n):
     if n == 0: return 0
     if n == 1: return 1
     if n in cache: return  cache[n]
     result = fib_cache(n-1) + fib_cache(n-2)
     cache[n]= result
     return result
print(fib_cache(9))