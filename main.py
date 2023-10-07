#If the bill was 150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00/5) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")
Bill = float(input("What was the total bill? $"))
Tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
People = int(input('How many people to split the bill? '))

# 1st Method
Bill_with_tip = (Bill) * (Tip / 100) + Bill
Bill_per_person = Bill_with_tip / People
Final_Amount = round(Bill_per_person, 2)

print(f"Each person should pay ${Final_Amount}")
print("Each person should pay: $", Final_Amount)

# 2nd Method
tip_as_percent = Tip / 100
total_tip_amount = Bill * tip_as_percent
total_bill = Bill + total_tip_amount
bill_per_person = total_bill / People
final_Amount = round(bill_per_person, 2)

print(f"Each person should pay ${final_Amount}")
