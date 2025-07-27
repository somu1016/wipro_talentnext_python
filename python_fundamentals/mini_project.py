# Project 1

while True:
    try:
        distance = int(input("How far would you like to travel in miles? "))
        if distance >= 0:
            break
        print("Please enter a positive number")
    except ValueError:
        print("Please enter a valid number")

if distance < 3:
    vehicle = "Bicycle"
elif distance < 300:
    vehicle = "Motor-Cycle"
else:
    vehicle = "Super-Car"

print(f"I suggest {vehicle} to your destination")

#Project 2




hourly_rate = 0.51

while True:
    try:
        budget = float(input("Enter your budget in $: "))
        if budget >= 0:
            break
        print("Please enter a positive amount")
    except ValueError:
        print("Please enter a valid number")

daily_cost = hourly_rate * 24
weekly_cost = daily_cost * 7
monthly_cost = daily_cost * 30
days_operable = budget / daily_cost

print("\nServer Operation Costs:")
print(f"- Per day: ${daily_cost:.2f}")
print(f"- Per week: ${weekly_cost:.2f}")
print(f"- Per month (30 days): ${monthly_cost:.2f}")
print(f"\nWith ${budget:.2f}, you can operate one server for {days_operable:.1f} days")