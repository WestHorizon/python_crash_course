names = ['Eric', 'Tom', 'Linda', 'Lucy', 'Messi']

for i in range(len(names)):
    output = f"Hello,\t{names[i]}"
    print(output)


names.append('Jerry')
print("==> After names.append('Jerry'):", names)

names.insert(2, 'Ann')
print("==> After names.insert(2, 'Ann'):", names)

print("==> names[3]:", names[3])
del names[3]
print("==> names[3]:", names[3])
print("==> After del names[3]:", names)

popped_names = names.pop()
print("==> names:", names)
print(popped_names)

popped_names = names.pop(0)
print("==> names:", names)
print(popped_names)

print("==> names[1]:", names[1])
names.remove(names[1])
print("==> names:", names)

names.sort()
print("==> names:", names)
names.sort(reverse=True)
print("==> names:", names)

names_sort = sorted(names)
print("==> names_sort:", names_sort)
print("==> names:", names)

names.reverse()
print("==> names:", names)


