# 2-3
user_name = 'Eric'
message = f"Hello {user_name}, would you like to learn some Python today?"
print("==> output:", message)

# 2-4
print(user_name.title())
print(user_name.lower())
print(user_name.upper())

# 2-5 & 2-6
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”
famous_person = 'Albert Einstein'
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print("==> outpuut:", message)

# 2-7
famous_person = '\tAlbert\t\n\tEinstein\t'
print(famous_person)
print(len(famous_person))
famous_person = famous_person.lstrip()
print(famous_person)
print(len(famous_person))
famous_person = famous_person.rstrip()
print(famous_person)
print(len(famous_person))
famous_person = famous_person.strip()
print(famous_person)
print(len(famous_person))