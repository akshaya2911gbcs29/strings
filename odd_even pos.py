s=input("Enter a string:")
odd=" "
even=" "
for i in range(len(s)):
    if i%2==0:
        even=even+ s[i]
    else:
        odd=odd + s[i]
print("Characters at even position:",even)
print("Characters at odd position:",odd)
