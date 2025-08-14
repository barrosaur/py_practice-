# A program that extracts and adds the two least significant digits of an integer

inp_num = int(input("Enter a number: "))

def extract_last_digit(number):
    return number % 10

def extract_second_ld(number):
    return int(((number % 100) - extract_last_digit(number)) / 10)

first_last_digit = extract_last_digift(inp_num)
second_last_digit = extract_second_ld(inp_num)
digit_sum = first_last_digit + second_last_digit

print(f"{first_last_digit} + {second_last_digit} = {digit_sum}")