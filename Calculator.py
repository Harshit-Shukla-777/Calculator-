#Python Calculator
operator = input(" Enter Your Operator(+ - * /): ")

num1 = float(input(" Enter the 1st number: "))
num2 = float(input(" Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result , 5))

elif operator == "-":
    result = num1 - num2
    print(round(result , 5))
    
elif operator == "*":
    result = num1 * num2
    print(round(result , 5))
    
elif operator == "/":
    result = num1 / num2
    print(round(result , 5))
    
else:
    print(f"{operator} isn't valid")
    
    
    