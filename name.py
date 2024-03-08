name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "Fabio"
last_name = "mich"

# USING VARIABLES IN STRINGS - F-STRINGS

full_name = f"{first_name} {last_name}"
print(full_name)

message = f"Hello, {full_name.title()}!"
print(message)

# ADDING WHITESPACE TO STRING WITH TABS OR NEWLINES

print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# STRIPPING WHITESPACE

# rstrip() strip whitespace from right side
# lstrip() strip whitespace from left side
# strip() strip whitespace from both sides

favorite_language = 'python '
print(favorite_language + "-")
print(favorite_language.rstrip() + "-")

# REMOVING PREFIXES

nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

# APOSTROPHE

message = "One of Python's strengths is its diverse community."
print(message)