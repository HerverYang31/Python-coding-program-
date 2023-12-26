def emailSlicer(email):
    username = email[:email.index("@")]
    domain = email[email.index("@")+1:]
    return f"Your username is {username}\nYour domain is {domain}"

#hyang@my.milligan.edu

email = str(input("Enter your email address: "))
print(emailSlicer(email))