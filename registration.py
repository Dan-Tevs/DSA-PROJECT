

def main():
    print("[1] Register")
    print("[2] Log In")

def register():
    print("REGISTRATION")
user = input("Enter username: ")
password = input("Password: ")
confirmpass = input("Confirm password: ")

while password != confirmpass:
    if password == confirmpass:  
        print("Registered!")     
    else:
        print("Password not match!") 
        ()
    
    

def login():
    pass

main()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
       register()