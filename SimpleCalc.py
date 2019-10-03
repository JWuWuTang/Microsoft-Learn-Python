#SimpleCalc is a very basic simple calculator that adds, subtracts, multiplies, 
# or divides two numbers

x = int(input("Please input your first number:"))
y = int(input("Please input your second number:"))
operation = input("Please indicate whether you want to add, subtract, multiply, or divide these numbers:")
upperOper = operation.upper()
if (upperOper == "ADD"):
    result = x + y
elif (upperOper == "SUBTRACT"): 
    result = x - y
elif (upperOper == "MULTIPLY"):
    result = x * y
elif (upperOper == "DIVIDE"):
    result = x / y
print(result)

#Remember that ":"" goes after the if statement
#Right now, when they input the operation, it must be in lowercase
#Must figure out how to make it accept lowercase and uppercase
#Use or statement? Is there another way to do this?
#Or statement causes operations to ONLY add
#If you make the input always uppercase, then you only have to set it to one string
