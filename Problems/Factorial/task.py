N = int(input())
count = 1
factorial = 1
while count <= N:
    factorial = factorial * count
    count += 1
print(factorial)

# another solution
# a = int(input())
# fact = a
# while a > 1:
#     a = a - 1
#     fact = fact * a
# print(fact)
