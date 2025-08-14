yearly_pay = float(input("Enter your yearly pay: "))

# There are 52 weeks in a year
weekly_pay = yearly_pay / 52

def pay_status(weekly_pay):
    if (weekly_pay < 5000):
        return "You poor 🔥"
    elif(weekly_pay < 20000):
        return "Minimum wage ass 🤒"
    elif(weekly_pay < 30000):
        return "Getting good. What do you do? 💼"
    elif(weekly_pay >= 30000):
        return "You're money laundering 🤑"
    else:
        return "Jackass. That ain't valid ⚠️"
    
ur_pay_stats = pay_status(weekly_pay)

print(f"Your weekly pay is: {weekly_pay}\nStatus: {ur_pay_stats}")