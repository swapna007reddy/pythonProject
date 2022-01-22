factorial = 5
num = 1
i = 1
while i <= factorial:
    num = num * i
    i = i + 1
print(num)

factorial = 6
num = 1
while 1 <= factorial:
    num = num * factorial
    factorial -= 1
print(num)

factorial = 6
num = 1
while 1 <= factorial:
    num = num * factorial
    factorial -= 1
print(num)


def fact_function(factorial):
    num = 1
    while 1 <= factorial:
        num = num * factorial
        factorial -= 1
    print(num)


fact_function(10)
fact_function(7)
fact_function(8)
fact_function(3)

# 0 1 1 2 3 5 8 13 21
#fabonacci series

num=0
def series():
    for i in range(num,20,num+1):
        print(num)

series()
