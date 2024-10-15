print("Secure login")
username = input("Username > ")
password = input("Password > ")                    # password   is added
if username == "mark" and password == "password":  # password is specified for mark    
    print("Welcome Mark!")    
elif username == "bug" and password == "3ug":  # password is specified for bug
        print("hey bug!")
else:
    print("Access denied!")
    