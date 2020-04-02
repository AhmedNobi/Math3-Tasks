#Author: Ahmed Nobi
#Second task
print("Before doing any thing read this note, please:")
print("please don't use any of these character:{a,n,d,o,r,i,m,b}")
print("To use \"Negation (not)\" write \"not\"")
print("To use \"Conjunction (and)\" write \"and\"")
print("To use \"Disjunction (or)\" write \"or\"")
print("To use \"Material implication (if...then)\" you must write the function like this: \"im(p,q)\"")
print("To use \"Biconditional (if and only if)\" you must write the function like this: \"bi(p,q)\"")
import itertools
import time
#Material implication function
def im (p,q):
    if not (p) or  (q) == True:
        return 1
    else:
        return 0
#Biconditional function
def bi (p,q):
    if (p and q) or (not(p) and not(q)) == True:
        return 1
    else:
        return 0
#Enter the number of symbols
print("Please enter the number of sympols:")
n = int(input())
variable_list = list()
i = 0
#Enter the symbols
print("Please enter the sympols seperated with new line:")
while i < n:
    variable_list.append(input())
    i += 1
#Enter the expression
print("Please enter the expression:")
expersion = input()
expersion2 = list(expersion)
table = list(itertools.product([0, 1], repeat=n))
x = 0
print("Truth Table")
while x < len(variable_list):
    print(variable_list[x], end='\t')
    x += 1
print(expersion)
jj = 0
kk = 0
j = 0
while j < 2 ** n:
    k = 0
    y = 0
    while k < n:
        t = 0
        print(table[j][k],end = "\t")
        for lett in expersion:
            if lett == variable_list[y]:
                expersion2[t] = table[j][k]
            t += 1
        k += 1
        i += 1
        y += 1
    j += 1
    str1 = ''.join(str(e) for e in expersion2)
    print(eval(str1))
time.sleep(5)