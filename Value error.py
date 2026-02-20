try:
    number=int(input("Enter the number:"))
    print("The number entered is", number)

except ValueError as ex:
    print("Exception:", ex)

    