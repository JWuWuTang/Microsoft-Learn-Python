print("I am learning how to code!")
help(print) #using the help function allows us to explore this command
x = 2 #assign variable x the value 2, this is an int
y = x + 5 #assign variable y the value x + 5
z = y #assign variable z the value y
a = 1.0 #assign variable a the value 1.0, this is a float
print(type(a)) #outputs float
print(type(x)) #outputs int
print(a*x) #when you multiply an int by a float, results in a float
print(type(a*x)) #outputs float

b = True #this is a boolean, remember you must capitalize the T in True
print(type(b)) #outputs "bool"

TestString = "This is a test string."
print(TestString)

FavAnime = input("Enter your favorite anime:") #Testing the input function
#When you input your favorite anime above, it inputs on the same line as the text
print(FavAnime) 

print("Enter your favorite anime:")
anime = input()
#When you input favorite anime, it inputs on the next line
print(anime)

FavNumber = int(input("Enter a number:")) #This will print the input as an int
print(FavNumber) #You must enter a number or it will fail