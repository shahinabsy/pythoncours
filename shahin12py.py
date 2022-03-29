Massage = input("Enter a massage:")
key = int(input("Enter key:"))
encrypted = " "
for letter in massage:
    encrypted += chr(ord(letter)+key)
    
print(encrypted)
