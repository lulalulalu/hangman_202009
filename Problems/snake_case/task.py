word = input()
res = []
for char in word:
    if char.isupper():
        res.append("_")
        res.append(char.lower())
    else:
        res.append(char)
print("".join(res))

# also
# list1 = input()
# for i in list(list1):
#     if i.isupper():
#         i = '_' + i.lower()
#     print(i, end='')
