try:
    year=int(input("Enter year you were born"))
    age=2026-year
    if age%2==0:
        print("Your age is an even number which is", age)

    else:
        print("Your age is an odd number which is",age)

except ValueError:
    print("Invalid input")