print("=== CALCULATOR ===")
num_1 = int(input("Enter num 1: "))
num_2 = int(input("Enter num 2: "))
operation = input("Operation: ")

def calculate(num1, num2, op):
  match op:
    case "+":
      return num1 + num2
    case "-":
      return num1 - num2
    case "*":
      return num1 * num2
    case "/":
      if num2 == 0:
        print("Cannot divide by 0.")
      else:
        return num1/num2
    case _:
      print("Invalid operation.")

result = calculate(num_1, num_2, operation)
print(f"Result: {result}")