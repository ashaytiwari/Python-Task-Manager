password = input('Enter Password: ')

results = []

if len(password) > 8:
    results.append(True)
else:
    results.append(False)

contains_digit = False

for i in password:
    if i.isdigit():
        contains_digit = True
        break
    
results.append(contains_digit)

contains_uppercase_char = False

for i in password:
    if i.isupper():
        contains_uppercase_char = True
        break
    
results.append(contains_uppercase_char)

if all(results):
    print("Strong Password")
else:
    print("Weak Password")