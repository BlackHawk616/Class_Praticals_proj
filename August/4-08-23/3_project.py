from time import sleep # You dont need to import and use this module 

# Writing A Program To Accept Radius And Calculate The Area Of Circle and Perimeter Of The Circle 

print(":: Welcome To Area Calulator And Perimter Calculator OF Circle")

print(":: please Enter The Radius Of The Circle")

radius = int(input(":: Enter the Radius Of The Circle :- ")) # Taking The Input Of Radius

pie = 3.14 # Its The Value Of Pie

area_of_circle = pie * radius * radius # Find The radius (*) Means Multiply

print(":: The Area Of Circle is :-", area_of_circle)

print(":: Now Calculating The Perimeter of The Circle")

perimeter = 2 * pie * radius

print(":: The Perimeter of The Circle is :- ", perimeter)

sleep(4)


