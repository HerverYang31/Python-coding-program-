
bill = int(input("How much is the bill today: "))
amount_people = int(input("How many people for today: "))
tips = round(bill *0.1,2)
tips_each_person = round(tips/amount_people,2)
bill = round(bill*1.1,2)
print("For the 10% tips, the tips will be",tips,", Total amount will be",bill)
print("Tips for each person will be",tips_each_person)