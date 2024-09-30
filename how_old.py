name = input("Hey whats your name? ")
age = int(input(f"Hey {name} how old are u? "))
if age <= 16:
    print("You can't drive.")
if age <= 18: 
    print("You can't vote.")
if age <= 21: 
    print ("You can't rent a car.")
if age >= 21:
    print("You can do anything that's legal.")