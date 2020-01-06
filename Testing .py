x = int(input('enter the first number'))
y = int(input('enter the second number'))

try:
    z = x / y
print(z)

except ZeroDivisionError:
print('Please dont enter zero')
