print("Welcome to Tip Calculator!")

bill = float(input("What is the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

tip_amount = bill * (tip_percent / 100)
total_bill = bill + tip_amount
amount_per_person = round(total_bill / num_people, 2)

print(f"Each person should pay: ${amount_per_person}")