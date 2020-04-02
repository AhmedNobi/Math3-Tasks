#Author: Ahmed Nobi
#First task
import time
print("Before doing any thing read this note, please:")
print("To use \"Negation (not)\" write \'-\'")
print("To use \"Conjunction (and)\" write \'&\'")
print("To use \"Disjunction (or)\" write \'|\'")
print("To use \"Material implication (if...then)\" write \'>\'")
print("To use \"Biconditional (if and only if)\" write \'<\'")
print()
#Enter the number of symbols
print("Please enter the number of symbols: ")
num_symbols = int(input())
#Enter the symbols
symbols = list()
print("Please enter the symbols seperated with new line: ")
i = 0
while i < (int(num_symbols)):
    n = input()
    symbols.append(n)
    i += 1
#Enter the expression
expression = str(input("Please enter the expression: "))
#Check the expression (not gate)
NOT = '-'
counter1 = 0
counter2 = 0
intial2 = 0
intial1 = 0
for n in expression:
    if n == NOT:
        expression = expression[:counter1 + intial2] + '(' + expression[counter1 + intial2:]
        intial2 += 1
    counter1 += 1
for n in expression:
    if n == '-':
        expression = expression[:counter2 + intial1 + 2] + ')' + expression[counter2 + intial1 + 2:]
        intial1 += 1
    counter2 += 1
#Check the experession (and gate)
AND = '&'
counter3 = 0
counter4 = 0
counter5 = 0
v = 0
vv = 0
while counter3 < len(expression) - 1:
    if expression[counter3] == AND:
        if expression[counter3 - 1] >= 'a' and expression[counter3 - 1] <= 'z':
            expression = expression[:counter3 - 1] + '(' + expression[counter3 - 1:]
            counter3 += 1
        if expression[counter3 + 1] >= 'a' and expression[counter3 + 1] <= 'z':
            expression = expression[:counter3 + 2] + ')' + expression[counter3 + 2:]
            counter3 += 2
    counter3 += 1
while counter4 < len(expression) - 1:
    if expression[counter4] == AND:
        if expression[counter4 - 1] == ')' and expression[counter4 + 1] >= 'a' and expression[counter4 + 1] <= 'z':
            v = counter4
            while v >= 0:
                if expression[v] == '(':
                    expression = expression[:v] + '(' + expression[v:]
                    counter4 += 1
                    break
                v -= 1
    counter4 += 1
while counter5 < len(expression) - 1:
    if expression[counter5] == AND:
        if expression[counter5 + 1] == '(' and expression[counter5 - 1] >= 'a' and expression[counter5 - 1] <= 'z':
            vv = counter5
            while vv < len(expression) - 1:
                if expression[vv] == ')':
                    expression = expression[:vv] + ')' + expression[vv:]
                    counter5 += 1
                    break
                vv -= 1
    counter5 += 1
#Check the experession (or gate)
AND = '|'
counter3 = 0
counter4 = 0
counter5 = 0
v = 0
vv = 0
while counter3 < len(expression) - 1:
    if expression[counter3] == AND:
        if expression[counter3 - 1] >= 'a' and expression[counter3 - 1] <= 'z':
            expression = expression[:counter3 - 1] + '(' + expression[counter3 - 1:]
            counter3 += 1
        if expression[counter3 + 1] >= 'a' and expression[counter3 + 1] <= 'z':
            expression = expression[:counter3 + 2] + ')' + expression[counter3 + 2:]
            counter3 += 2
    counter3 += 1
while counter4 < len(expression) - 1:
    if expression[counter4] == AND:
        if expression[counter4 - 1] == ')' and expression[counter4 + 1] >= 'a' and expression[counter4 + 1] <= 'z':
            v = counter4
            while v >= 0:
                if expression[v] == '(':
                    expression = expression[:v] + '(' + expression[v:]
                    counter4 += 1
                    break
                v -= 1
    counter4 += 1
while counter5 < len(expression) - 1:
    if expression[counter5] == AND:
        if expression[counter5 + 1] == '(' and expression[counter5 - 1] >= 'a' and expression[counter5 - 1] <= 'z':
            vv = counter5
            while vv < len(expression) - 1:
                if expression[vv] == ')':
                    expression = expression[:vv] + ')' + expression[vv:]
                    counter5 += 1
                    break
                vv -= 1
    counter5 += 1
#Check the experession (imply gate)
AND = '>'
counter3 = 0
counter4 = 0
counter5 = 0
v = 0
vv = 0
while counter3 < len(expression) - 1:
    if expression[counter3] == AND:
        if expression[counter3 - 1] >= 'a' and expression[counter3 - 1] <= 'z':
            expression = expression[:counter3 - 1] + '(' + expression[counter3 - 1:]
            counter3 += 1
        if expression[counter3 + 1] >= 'a' and expression[counter3 + 1] <= 'z':
            expression = expression[:counter3 + 2] + ')' + expression[counter3 + 2:]
            counter3 += 2
    counter3 += 1
while counter4 < len(expression) - 1:
    if expression[counter4] == AND:
        if expression[counter4 - 1] == ')' and expression[counter4 + 1] >= 'a' and expression[counter4 + 1] <= 'z':
            v = counter4
            while v >= 0:
                if expression[v] == '(':
                    expression = expression[:v] + '(' + expression[v:]
                    counter4 += 1
                    break
                v -= 1
    counter4 += 1
while counter5 < len(expression) - 1:
    if expression[counter5] == AND:
        if expression[counter5 + 1] == '(' and expression[counter5 - 1] >= 'a' and expression[counter5 - 1] <= 'z':
            vv = counter5
            while vv < len(expression) - 1:
                if expression[vv] == ')':
                    expression = expression[:vv] + ')' + expression[vv:]
                    counter5 += 1
                    break
                vv -= 1
    counter5 += 1
#Check the experession (bio gate)
AND = '<'
counter3 = 0
counter4 = 0
counter5 = 0
v = 0
vv = 0
while counter3 < len(expression) - 1:
    if expression[counter3] == AND:
        if expression[counter3 - 1] >= 'a' and expression[counter3 - 1] <= 'z':
            expression = expression[:counter3 - 1] + '(' + expression[counter3 - 1:]
            counter3 += 1
        if expression[counter3 + 1] >= 'a' and expression[counter3 + 1] <= 'z':
            expression = expression[:counter3 + 2] + ')' + expression[counter3 + 2:]
            counter3 += 2
    counter3 += 1
while counter4 < len(expression) - 1:
    if expression[counter4] == AND:
        if expression[counter4 - 1] == ')' and expression[counter4 + 1] >= 'a' and expression[counter4 + 1] <= 'z':
            v = counter4
            while v >= 0:
                if expression[v] == '(':
                    expression = expression[:v] + '(' + expression[v:]
                    counter4 += 1
                    break
                v -= 1
    counter4 += 1
while counter5 < len(expression) - 1:
    if expression[counter5] == AND:
        if expression[counter5 + 1] == '(' and expression[counter5 - 1] >= 'a' and expression[counter5 - 1] <= 'z':
            vv = counter5
            while vv < len(expression) - 1:
                if expression[vv] == ')':
                    expression = expression[:vv] + ')' + expression[vv:]
                    counter5 += 1
                    break
                vv -= 1
    counter5 += 1
print(' ' + expression + ' ')
time.sleep(5)