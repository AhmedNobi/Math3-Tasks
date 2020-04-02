#Author: Ahmed Nobi
#Third task
import time
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
print("Please enter the number:")
n = int(input())
i = 2
print("The Primes are")
while i < n:
    if isPrime(i) and isPrime(n-i):
        print(int (i))
        print((int)(n-i))
        break
    i += 1


time.sleep(5)