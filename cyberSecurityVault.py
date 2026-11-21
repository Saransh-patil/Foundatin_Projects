name=input("Enter your name ")
print("Welcome ",name," in our Security Vault")
w=0
p=0
while True:
    print(name," Here are the Services")
    print("Enter 1 for login and reset password")
    print("Enter 2 for Checking History")
    print("Enter 3 for adding Confidential Data")
    print("Enter 4 to exit")
    f=int(input("Please select any one facility"))
    match f:
        case 1:
            print("\nYou have entered in Login & Reset field")
            pwd=1234
            c=0
            while True:
                n=int(input("\nPlease enter your password"))
                if n==pwd:
                    print("\nWelcome admin in your control panel")
                    new=int(input("\nPlease enter new password"))
                    pwd=new
                    print("Password updated successfully")
                    p+=1
                    break
                else:
                    c+=1
                    w+=1
                    print("\nWrong password")
                    if c>2:
                        print("Authentication failed")
                        break
            if c>2:
                break
        case 2:
            print("\nYou have entered Security Checking field")
            print("History")
            print(w," times wrong authentication happened")
            print(p," times password was changed by admin")
            break
        case 3:
            print("\nSecurity Vault Activated")
            d1=input("Enter data")
            print("Data saved successfully")
            no=int(input("Enter 1 to see data and 2 to exit"))
            match no:
                case 1:
                    if d1=='':
                        print("No data added")
                        break
                    else:
                        print(d1)
                        break
                case 2:
                    break
        case 4:
            print(name, " You have exited successfully")
            break 

