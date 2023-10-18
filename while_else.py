num = 10
while num <= 11:
    print(f"{num} is less than or equal to 11")
    num += 1
else:
    print(f"{num} is greater than 11")


teachers = ["Lee","Smith", "Brown"]
for ele in teachers:
    if ele in teachers == "Choi":
        print("Choi is the teacher")
        break
    else:
        print("Not found Choi")