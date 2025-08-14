units_sem_1 = int(input("Enter units for the 1st sem: "))
units_sem_2 = int(input("Enter units for the 2nd sem: "))

# additional fees
reg_fee = 450
per_unti = 450
penalty = 2260

def calculate_sem_fee(units):
    return 450 + (450 * units) + (units * 2260)/float(12)

first_sem_fee = calculate_sem_fee(units_sem_1)
second_sem_fee = calculate_sem_fee(units_sem_2)

print(f"1st Semester Tuition fee: {first_sem_fee}")
print(f"2nd Semester Tuition fee: {second_sem_fee}")
print(f"Total tuition fee: {first_sem_fee + second_sem_fee}")