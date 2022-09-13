name = "ada lovelace"
print("==> name:", name)

print("==> name.title():", name.title())
print("==> name.upper():", name.upper())
print("==> name.lower():", name.lower())

name = "aDa lOvELace"
print("==> name:", name)
print("==> name.tile():", name.title())


first_name = "ada"
last_name = "lovelace"
# After py3.6
full_name = f"{first_name} {last_name}"
print("==> full_name:", full_name)
print(f"Hello,{full_name}!")
message = f"Hello,{full_name}!"
print("==> message:", message)

# Before py3.5
full_name = "{} {}".format(first_name, last_name)
print("==> full_name:", full_name)

