def add(a,b):
    return a+b

c=add(5,6)
print(c)

x=lambda a,b: a+b
print(type(x))
z=x(5,16)
print(z)

def mul():
    return lambda a,b:a%b
c=mul()
print(c(15,5))

# def myrange():
#     return lambda a: list(myrange(1,a+1)
#
# prib
