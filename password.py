password=input("Enter password:")
has_digit=False
has_lower=False
has_upper=False
has_special=False
special_char="@#%&!$"
if len(password)<8 or len(password)>15:
    print("Invalid Password")
    exit()
for ch in password:
    if ch.isdigit():
        has_digit=True
    elif ch.islower():
        has_lower=True
    elif ch.isupper():
        has_upper=True
    elif ch in special_char:
        has_special=True
    elif ch==" ":
        print("Invalid Character")
        exit()
if has_digit and has_lower and has_upper and has_special:
    print("valid Password")
else:
    print("Invalid Password")
