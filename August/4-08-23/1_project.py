from time import sleep

# Writing A Program to accept principal, rate of interest and time and caluclating simple years

print("Welcome to simple interset calculator")

print("Enter The principal value here")

principal = int(input(":- Enter Here : ")) # Taking The Input Of Principal Value from user

print("Enter The Rate of interest")

rate_of_interset = float(input(":- Enter Here : ")) # Taking The Input of Rate Of Interset from user

print("Enter The Time Period (In Years)")

ti_me = int(input(":- Enter Here : ")) # Taking input of time period from user

simple_interest = (principal * rate_of_interset * ti_me) / 100 # using simple interest formula

print("Your Simple Interset Is :- ",simple_interest)

