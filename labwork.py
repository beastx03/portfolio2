# Task 1
name = input ("What's your name? : ")
print("Hello", name,". Welcome to the program")
print("_______________________________________________")

# Task 2
celsius = input("Please enter a temperature in celsius: ")
print("Converting celsius to fahrenheit...")
fahrenheit = (float(celsius)*9/5 + 32)
print (celsius,"Celsius is",fahrenheit ,"Fahrenheitah.")
print("_______________________________________________")

# Task 3
student = int(input("How many students? : "))
group = int(input("How many students per group? : "))
pergroup = student//group
leftover = student%group
if leftover < 2:
    print("There will be", pergroup,"groups and", leftover,"student left over.")
else:
    print("There will be", pergroup,"groups and", leftover,"students left over.")
print("_______________________________________________")

# Task 4
candy = int(input("What is the number of candy? : "))
students = int(input("What is the number of students? : "))
giveout = candy//students
leftovers = candy%students
print("Give", giveout, "to each student. You will have", leftovers,"candy left over.")