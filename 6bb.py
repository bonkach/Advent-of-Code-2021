from functools import wraps
def memoize(function):    
    memo = {}
        
    @wraps(function)
    def wrapper(*args):

        # add the new key to dict if it doesn't exist already  
        if args not in memo:
            memo[args] = function(*args)

        return memo[args]

    return wrapper
    
    
@memoize
def f(a, n):
    if a > n:
        return 1
    else:
        return f(a + 9, n) + f(a + 7, n)

ulaz = open('ulaz.txt', 'r')
sve = ulaz.read()
sve = list(map(int, sve.split(',')))
ulaz.close()
n = 256
br = 0
for a in sve:
    br += f(a + 1, n)
print(br)
    
    
         
