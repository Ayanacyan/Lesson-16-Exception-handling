try:
    num1,num2=eval(input("Enter two numbers, seperated by a comma: "))
    result=num1/num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by 0 is error!!")

except SyntaxError:
    print("Comma is missing. Enter the numbers seperated by commas like this 6,7")

except:
    print("Wrong input!")

else:
    print("No exceptions")

finally:
    print("This will still definetely execute!")