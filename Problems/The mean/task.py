entries = 1
total = 0
while True:
    numbers = input()
    if numbers == ".":
        break
    total = total + int(numbers)
    res = total / entries
    entries += 1
print(res)

# another solution
numbers = []
a = input()
while a != '.':
    numbers.append(int(a))
    a = input()
print(sum(numbers) / len(numbers))
