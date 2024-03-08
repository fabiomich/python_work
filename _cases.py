# Personal message
name = "pepito perez"
print(f"Hello {name}, would you like to learn some Python today?\n")

# Name cases
print(f"lowercase: {name.lower()}")
print(f"upercase: {name.upper()}")
print(f"title: {name.title()}")

# FAMOUS QUOTE
message = 'Albert Einstein once said, "A person who never made a mistake never tried anything new"'
print(message)

# FAMOUS QUOTE 2
famous_person = 'Fabian Einstein'
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new"'
print(message)

# STRIPPING NAMES
person_name = '\t Fabio mich   \n   '

print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())

# FILE EXTENSIONS
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))

print(5+3)
print(12-4)
print(4*2)
print(32/4)

fav_num = 9
print(f"My fav num is {fav_num}")
