
# def tryrecursion(num):
#     if num == 0:
#         print("all nums are printed")
#     else:
#         print("!")
#         tryrecursion(num-1)
#         print(num)


# num = 5

# tryrecursion(num)




def firstMethod():
    secondMethod()
    print("I am the first Method")

def secondMethod():
    thirdmethod()
    print("I am the second Method")

def thirdmethod():
    fourthMethod()
    print("I am the third Method")

def fourthMethod():
    print("I am the fourth method")


firstMethod()


# def recursionMethod(n):
#     if n<1:
#         print("n is less than 1")
#     else:
#         recursionMethod(n-1)
#         print(n)

# recursionMethod(5)

# def fib(n):
#     a = 0
#     b = 1
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         for _ in range(1,n):
#             c = a + b
#             print(c)
#             a = b
#             b = c 
#         return c
    
# print(fib(9))

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# print(fib(10))

# def powerOfTwo(n):
#     if n == 0:
#         return 1
#     else:
#         power = powerOfTwo(n-1)
#         return power * 2
    

# print(powerOfTwo(3))


# power = 1
# n = 3

# for i in range(3):
#     power = power * 2

# print(power)

# How to write recursion in 3 steps

# def factorial(n):
#     assert n >= 0 and int(n) == n, "The number mush be positive integer only!"
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    

# print(factorial(4))


# def findMaxNumRec(sampleArray, n):
#     if n == 1:
#         return sampleArray[0]
#     return max(sampleArray[n-1], findMaxNumRec(sampleArray,n-1))

# sampleArray = [10,25,1,2,3,22,1]

# print(findMaxNumRec(sampleArray,len(sampleArray)))


# def sumofdigits(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return n + sumofdigits(n-1)

# print(sumofdigits(5))
# print(sumofdigits(0))
# print(sumofdigits(1))
# print(sumofdigits(10))


# def simpleSumofdigit(n):
#     return n * (n+1)/2

# print(simpleSumofdigit(20))


# def sumofdigits(n):
#     assert n>=0 and int(n) == n , "The number should be positive integer"
#     if n == 0:
#         return 0
#     else:
#         return n%10 + sumofdigits(n//10)
    
# print(sumofdigits(-112))
# print(sumofdigits(12))
# print(sumofdigits(1))
# print(sumofdigits(555))




# def power(n,t):
#     assert int(t) == t , "The no should be in integer"
#     if t == 0:
#         return 1
#     return n * power(n,t-1)
# print(power(3,4))



# def gcd(a,b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a%b)


# print(gcd(100,50))


# def decimal_to_binary(n):
#     binary_num = ""
#     while n > 0:
#         remainder = n % 2
#         binary_num = str(remainder) + binary_num
#         n = n // 2
#     return binary_num

# print(decimal_to_binary(10))


# def decimal_to_binary(n):
#     if n == 0:
#         return 0
#     else:
#         return n%2 + 10 * decimal_to_binary(int(n/2))
    

# print(decimal_to_binary(10))
