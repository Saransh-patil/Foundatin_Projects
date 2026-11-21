print("Welcome to digital Evidence System")
pwd=1234
print("Password is required ")
c=0
e=''
eid=0
while True:
    p=int(input("Enter password"))
    if p==pwd:
        while True:
            print("Enter 1 to upload evidence")
            print("Enter 2 to see the evidence")
            print("Enter 3 to update evidence id")
            print("Enter 4 to update evidence")
            print("Enter 5 to exit")
            num=int(input("Select the option"))
            match num:
                case 1:
                    e=input("\nEnter data ")
                    eid+=1
                    print("Evidence uploaded successfully with id ",eid)
                case 2:
                    print("\nEvidence id = ",eid)
                    print("data = ",e)
                case 3:
                    print("\nYour current evidence id is ",eid)
                    new=int(input("Enter new evidence id"))
                    eid=new
                    print("New evidence id is updated successfully")
                case 4:
                    print("\nYour evidence is ",e)
                    new=input("Enter evidence")
                    e=new
                    print("Evidence updated successfully")
                case 5:
                    break
        break
    else:
        print("Wrong password")
        c+=1
        if c>2:
            print("Authentication failed")
            break
