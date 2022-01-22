# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)
#
# result=fact(5)
# print(result)


# def prime(n):
#     if n % 2 == 0:
#         return
#     print("given number is not a prime")
# else:
#     print("given number is a prime")
# result = prime(7)
# print(prime)


def simplerecursion(input):
    if input == 0:
        return 1
    else:
        #print(input * simplerecursion(input - 1))
        return input * simplerecursion(input - 1)

#print(simplerecursion(3))
