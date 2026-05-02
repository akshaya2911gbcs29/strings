text=input("Enter string:")
result=" "
letter=" "
for ch in text:
     if ch.isalpha():
         letter=ch
     elif ch.isdigit():
         result+=letter*int(ch)
print("Output:",result)
