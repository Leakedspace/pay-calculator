def get_hours(prompt):
    return float(input(prompt))

def weekday_pay(hours):
    return hours * WEEKDAY_RATE

def weekend_pay(hours):
    return hours * WEEKEND_RATE

def after_tax(total_pay, TAX_PERCENTAGE):
    return total_pay * TAX_PERCENTAGE / 100

WEEKDAY_RATE = float(input("What is your weekday rate: "))
WEEKEND_RATE = float(input("What is your weekend rate: "))
TAX_PERCENTAGE = float(input("What is your tac percentage: "))

week_hours = get_hours("What are your total weekday hours: ")
weekend_hours = get_hours("What are your total weekend hours: ")

week_pay = weekday_pay(week_hours)
weekend_pay_total = weekend_pay(weekend_hours)
total_pay = week_pay + weekend_pay_total
tax_paid = after_tax(total_pay, TAX_PERCENTAGE)
take_home = total_pay - tax_paid

print(f"Weekday: {week_hours} hours -> ${week_pay:.2f}")
print(f"Weekend: {weekend_hours} hours -> ${weekend_pay_total:.2f}")
print(f"Total gross pay -> ${total_pay:.2f}")
print(f"Total income after tax -> ${tax_paid:.2f}")
print(f"you take home pay is -> ${take_home:.2f}")
