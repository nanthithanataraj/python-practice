username = input("Enter username : ")
pwd = input("Enter pwd : ")
if username == 'admin':
    if pwd == '12345':
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Invalid username")