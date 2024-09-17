print("I have a class of 33 students.")
print("There are 11 girls, so that means..")
# 33-11 basic subraction
print(f"there are {33 - 11} boys.")
print()
#printed text including the round()function rounding 11 divided by 33 to two decimals places
print(f"That means {round((11 / 33 *100),2)}% are girls...")
#printed text including the percentage round()function rounded the number to two decimals
print(f"and {round(((33-11)/33*100),2)} % are boys.")
print()
print("If we made groups of six...")
# prints (33//6 divides 33 by 6 then rounds it to the nearest interger = 5
print(f"There would be {33 // 6} groups of six.")
#prints the remainder of 33/6 
print(f"And then a smaller group of {33 % 6} people.")
print("-" * 30)
print("If we had 17 apples and 3 people...")
# 17 // 3 divides 17 by 3 through floor division where it shows the whole number that 3 is able to go into 17  
print(f"Each person would get {17 // 3} whole apples.")
# 17 % 3 is a modulus where it shows the remainder of 17 divded by 3
print(f"There would be {17 % 3} apples remaining.")
print()
print("If we charged each person $2 each for their 5 apples..")
# 2 multiplied by 5 
print(f"they would each pay ${2*5}.")