# define the function,needed: add sub, mul,div
# print options to the users
# ask for values
# call the functions
# While loop to continue the program until the user wants to exit

# Step by step

def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer))


def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer))


def mult(a, b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer))


def div(a, b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer))


print("A,Addition")
print("B, Subtraction")
print("C, Multiplication")
print("D,Division")
print("E,Exit")

choice=input("Enter your choice: ")

if choice == "A" or choice == "a":
        print("Addition")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        add(a, b)

elif choice == 'B' or choice == "b":
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        sub(a,b)

elif choice == "C" or choice == "c":
        print("Multiplication")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        mult(a, b)

elif choice == "D" or choice == "d":
     print("Division")
     a = int(input("Enter first number: "))
     b = int(input("Enter second number: "))
     div(a, b)

elif choice == "E" or choice == "e":
     print("Program is ended")

quit()

