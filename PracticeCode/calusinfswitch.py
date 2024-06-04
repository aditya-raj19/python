f=float(input("Enter First Number "))
s=float(input("Enter Second Number "))
c=int(input("Select The Operation you want to perform \n 1.Add \n 2.Substraction\n 3.Multiplication\n 4.Division\n"))
match c:
    case 1:
        print(f+s)
    case 2:
        print(f-s)
    case 3:
        print(f*s)
    case 4:
        print(f/s)
    case _:
        print("Not a valid")