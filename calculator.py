number1 = float(input("Enter the first number: "))
operator = (input("Select an operator: "))
number2 = float(input("Enter the second number: "))

while True:
        if operator not in ("+","-","/","*") :
                print("Please select a valid operator")
                operator = input("Select an operator: ")
        elif ("+") in operator:
                result = number1 + number2
        elif ("-") in operator:
                result = number1 - number2
        elif ("/") in operator:
                if number2 == 0:
                        print("Can't divide by 0. Enter a different number")
                        number2 = float(input("Enter the second number: "))
                        continue        
                result = number1/number2

        elif ("*") in operator:
                result = number1 * number2
        break

print("The answer is", result)


    