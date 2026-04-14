print("Select your ride: ")
print("1. Bike")
print("2. Car")

#take input of number 1 or 2 
#select your ride 
choice = int( input("Enter your choice: "))

#User entering option 1
if( choice ==1 ): #condition 1 outer if statement
print("What type of bike: ")
print("1. Scooty\n")
print("2. scooter\n")

#Condition for selecting the type of bike 
choice2= int(input("Enter you choice2: "))
if choice2==1: #inner if statement 
    print("you have selcted scooty")
else:
    print("you have selcted scooter")

#User entering option 2
if( choice == 2 ): #outer elif statement
print("What type of car: ")
print("1. Sedan")
print("2. XUV")
choice2= int(input("Enter you choice2: "))

if choice3==1: #inner if statement 
    print("you have selcted sedan")
else:
    print("you have selcted XUV")

else: #outer else statement
print("Wrong choice!")

