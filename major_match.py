def major_match():
    major = str(input("What is your major: "))

    match major:
        case "CS":
            print("Your major is Computer Science")
        case "IS":
            print("Your major is Computer System") 
        case "EE":
            print("Your major is Computer Science") 
        case "ME":
            print("Your major is Computer Science")  
        case "POSC":
            print("Your major is Computer Science")
        case _:
            print("I don't know")

major_match()