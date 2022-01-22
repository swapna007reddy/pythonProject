num= 13
for i in range(2,num):
    if num %i==0:
        print("Given number is not a prime")
        break
else:
    print("Given number is prime")

# *****recursive prime number**********

def prime(n):
     if n% 2==0:
         print("given number is not a prime")
     else:
         print("given number is prime")

result=prime(7)
print(prime)


