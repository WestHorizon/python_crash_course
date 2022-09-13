name = "ada lovelace"
print("==> name:", name)

print("==> name.title():", name.title())
print("==> name.upper():", name.upper())
print("==> name.lower():", name.lower())

name = "aDa lOvELace"
print("==> name:", name)
print("==> name.tile():", name.title())


# 2.3.2 在字符串中使用变量
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


# 2.3.3 使用制表符或换行符来添加空白
print("Python")
print("\tPython")

print("Language:\nPython\nC\nJavaScript")

print("Language:\n\tPython\n\tC\n\tJavaScript")


# 2.3.4 删除空白
favorite_language = 'python    '
print("==> favorite_language:", favorite_language)
print("==> favorite_language.rstrip():", favorite_language.rstrip())
print("==> favorite_language:", favorite_language)
favorite_language = favorite_language.rstrip()
print("==> favorite_language:", favorite_language)

favorite_language = '    python'
print("==> favorite_language:", favorite_language)
print("==> favorite_language.rstrip():", favorite_language.lstrip())
print("==> favorite_language:", favorite_language)
favorite_language = favorite_language.lstrip()
print("==> favorite_language:", favorite_language)