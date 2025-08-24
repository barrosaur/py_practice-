num = int(input("Enter num: "))

def factorial(num):
  if(num == 0):
    return 1
  
  return num * factorial(num - 1)

print(f"Factorial: {factorial(num)}")