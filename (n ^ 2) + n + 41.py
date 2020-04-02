#Author: Ahmed Nobi
#Fourth task
import time
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
print("Please enter the number:")
n = int(input())
print("The result of \"(n ^ 2) + n + 41\" = ", n**2+n+41)
i = 2
if isPrime(n**2+n+41):
    print("This is a prime number")
else :
    while i < n**2+n+41:
        if (n**2+n+41) % i == 0:
            print("This number is not prime")
            print("This number is divisible by ", i)
            break
        i += 1


time.sleep(5)