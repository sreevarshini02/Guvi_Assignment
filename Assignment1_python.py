import re
import csv

inpt=int(input("Enter 1 for Registration or 2 for Login:"))
aa = []

if inpt==1:
    a=input("Enter your username/email id: ")
    with open("assignment1.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if(row[0]==a):
                 aa.append(row[0])
    if len(aa)>0:
        print("User name already exists. Choose a different user name")
    else:
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if '@' in a:
            a2 = a.split('@')
            if len(a2[0]) == 0:
                print("Enter valid username. First name missing.")
            else:
                if a2[1][0] == '.':
                    print("Enter valid username. There should not be '.' immediately next to '@'")
                else:
                    if a2[0][0].isalpha() == False:
                        print("Username cannot start with numbers or special characters")
                    else:
                        b = input("Enter the password:")
        else:
            print('Enter a valid username. @ is missing ')

        if len(b) < 5 or len(b) > 16:
            print("Invalid password. Password length should be between 5 to 16")
        else:
            if (regex.search(b) == None):
                print("Password should contain minimum one special character")
            else:
                res = [char for char in b if char.isupper()]
                if len(res) == 0:
                    print("Password should contain minimum one upper case character")
                else:
                    res = [char for char in b if char.islower()]
                    if len(res) == 0:
                        print("Password should contain minimum one lower case character")
                    else:
                        res = [char for char in b if char.isnumeric()]
                        if len(res) == 0:
                            print("Password should contain minimum one digit")
                        else:
                            with open('assignment1.csv', 'a', newline="") as file:
                                myFile = csv.writer(file)
                                myFile.writerow([a, b])
                                #data = pd.read_csv("assignment1.csv")
                                #print(data)
                                print("You have registered successfully")
elif inpt==2:
    a = input("Enter your username/email id: ")
    with open("assignment1.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if(row[0]==a):
                 b2=row[1]
                 b=input("Enter the password:")
                 if b==b2:
                     print("Logged in successfully")
                 else:
                     c=int(input("Invaid password! Type 1 if you have forgot your password else type 2:"))
                     if c==1:
                        print(b2)
            else:
                print("Username/email id not found. Please register yourself to continue login")
else:
    print("Enter valid input")