# Password Checking 
password = input("Enter your password:")
has_length = len(password)>=6
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
if has_length and has_digit and has_upper and has_lower:
  print("Strong Password")
else:
    print("Weak password. Please change")
    if(not has_length):
        print("The length of the password must be 6")
    if(not has_digit):
        print("The password does not contain any digits. Please insert a digit.")
    if(not has_upper):
        print("The password does not contain any uppercase letters. Please insert an upper case letter.")
    if(not has_lower):
        print("The password does not contain any lowercase letters. Please insert a lower case letter.")
