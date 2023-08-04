from time import sleep #You dont need to import and use this module 

# Writing a Program to calculate the volume of cube

print("Welcome To Volume Calulator Of Cube Programm")

print(" Enter The side of cube")

side = int(input("Enter The Side Legnth OF Cube :- "))

volume = side * side * side

print("Volume Of Cube Is :-", volume)

print("Enter The Radius Of Cylinder")

rc = int(input("Enter Here :- "))

print("Enter The Height Of The cylinder")

hc = int(input("Enter Here :- "))

pie = 3.14

vlc = pie * rc * rc * hc

print("The Volume Of Cylinder is ", vlc)

print ("Enter The Length, height and width of Cuboid")

l = int(input("Enter Length Here :- "))

w = int(input("Enter Width Here :- "))

h = int(input("Enter Height Here :- "))

vol = l * w * h

print("The Volume Of Cuboid Is ", vol)