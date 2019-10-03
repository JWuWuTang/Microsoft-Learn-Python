#SimpleCalc is a very basic simple calculator that adds, subtracts, multiplies, 
# or divides two numbers

x = int(input("Please input your first number:"))
y = int(input("Please input your second number:"))
operation = input("Please indicate whether you want to add, subtract, multiply, or divide these numbers:")
if (operation == "add"):
    result = x + y
elif (operation == "subtract"): 
    result = x - y
elif (operation == "multiply"):
    result = x * y
elif (operation == "divide"):
    result = x / y
print(result)

#Remember that ":"" goes after the if statement
#Right now, when they input the operation, it must be in lowercase
#Must figure out how to make it accept lowercase and uppercase
#Use or statement? Is there another way to do this