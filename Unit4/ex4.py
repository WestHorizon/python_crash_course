squares = [value**2 for value in range(1,11)]
print(squares)

# ex4-3
for value in range(1, 21):
    print(value)


# ex4-4
values = list(range(1, 101))
for big_value in values:
    if big_value%10==0:
        print(f"{big_value}", end = '\n')
    else:
        print(f"{big_value}", end = '\t')

# ex4-5
min_value = min(values)
max_value = max(values)
sum_value = sum(values)
print(f"min: {min_value}; max:{max_value}; sum:{sum_value}")

# ex4-6
print("==> ex4-6")
odd_values = list(range(1, 21, 2))
for odd_value in odd_values:
    print(f"{odd_value}", end = '\t')

# ex4-7
print("\n==> ex4-7")
tri_values = list(range(3, 31, 3))
for tri_value in tri_values:
    print(f"{tri_value}", end = '\t')

# ex4-8 & 4-9
print("\n==> ex4-8 & 4-9")
values = [value**3 for value in range(1,11)]
print(values)
for value in values:
    print(value, end = '\t')

# ex4-10
print("==> ex4-10")
print(f"The first three items in the list are: {values[:3]}")
print(f"Three items from the middle of the list are: {values[4:7]}")
print(f"The last three items in the list are: {values[-3:]}")

# ex4-11
print("==> ex4-10")
my_colors = ['red', 'blue', 'green', 'yellow']
friend_colors = my_colors[:]
print(f"my_colors: {my_colors[:]}")
print(f"friend_colors: {friend_colors[:]}")
my_colors.append('pink')
friend_colors.append('purple')
print(f"my_colors: {my_colors[:]}")
print(f"friend_colors: {friend_colors[:]}")