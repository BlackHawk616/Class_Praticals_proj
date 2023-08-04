from time import sleep #You dont need to import and use this module 

# Writing a program to accept the marks in 5 subjects and calculate the total marks and verage marks 

print(":: Welcome To Total Marks And average Marks Calulator Program")

print(": Enter The marks of English")

eng = int(input(":: Enter the Marks Here :- "))

print(": Enter The marks of Maths")

maths = int(input(":: Enter the Marks Here :- "))

print(": Enter The marks of Physics")

physics = int(input(":: Enter the Marks Here :- "))

print(": Enter The marks of chemistry")

chemisty = int(input(":: Enter the Marks Here :- "))

print(": Enter The marks of Computer Science")

cs = int(input(":: Enter the Marks Here :- "))

total_marks = eng + maths + physics + chemisty + cs

print(" Total Marks :- ", total_marks)

avg = float(total_marks / 5)

print("Your Average Marks Is :- ", avg)

sleep(4)