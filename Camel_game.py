import random


print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and outrun the natives.")
print("-" * 72)


# variables
done = False
miles_traveled = 0
thirst = 0
camel_tiredness = 0
drinks_in_canteen = 3
natives_distance = -20
health = 10


while not done:
    # Weather condition effect
    weather_conditions = ["clear", "sandstorm", "heatwave"]
    weather = random.choice(weather_conditions)


    print(f"\nWeather condition: {weather}")
    if weather == "sandstorm":
        print("A sandstorm is slowing you down!")
    elif weather == "heatwave":
        print("It's extremely hot, your camel is tiring quickly!")
        camel_tiredness += random.randint(1, 3)


    print("")
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop and rest for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    print("-" * 30)
    
    user_choice = input("Please choose a letter: ").strip().capitalize()


    # Check for quit
    if user_choice == "Q":
        done = True


    # Status check
    elif user_choice == "E":
        print("")
        print(f"Miles traveled: {miles_traveled}")
        print(f"Drinks in canteen: {drinks_in_canteen}")
        print(f"Your camel's tiredness is {camel_tiredness}")
        print(f"Health: {health}")
        print(f"The natives are {natives_distance} miles behind you.")


    # Stop and rest for the night
    elif user_choice == "D":
        print("You stop to rest for the night. Your camel is happy.")
        camel_tiredness = 0  # Reset camel's tiredness
        natives_distance += random.randint(7, 14)  # Move natives forward randomly


    # Drink from canteen
    elif user_choice == "A":
        if drinks_in_canteen > 0:
            print("You take a drink from your canteen.")
            drinks_in_canteen -= 1
            thirst = 0  # Reset thirst
        else:
            print("You have no drinks left in your canteen!")


    # Moderate speed
    elif user_choice == "B":
        miles = random.randint(5, 12)
        miles_traveled += miles
        thirst += 1
        camel_tiredness += random.randint(1, 3)
        natives_distance += random.randint(7, 14)
        print(f"You traveled {miles} miles at moderate speed.")


    # Full speed
    elif user_choice == "C":
        miles = random.randint(10, 20)
        miles_traveled += miles
        thirst += 1
        camel_tiredness += random.randint(1, 3)
        natives_distance += random.randint(7, 14)
        print(f"You traveled {miles} miles at full speed.")


    else:
        print("Invalid choice, please select a choice that is listed.")


    # Random chance of finding an oasis
    if random.randint(1, 20) == 1:
        print("You've found an oasis! Your canteen is refilled, your thirst is quenched, and your camel is rested.")
        drinks_in_canteen = 3
        thirst = 0
        camel_tiredness = 0


    # Random encounters
    if random.randint(1, 15) == 1:
        print("You encounter a merchant!")
        choice = input("Do you want to trade? (Y/N): ").strip().upper()
        if choice == "Y":
            print("You traded some water for a magical map!")
            drinks_in_canteen += 1


    # Thirst checks
    if thirst > 4:
        print("You are thirsty.")
    if thirst > 6:
        print("You died of thirst!")
        done = True


    # Health check
    if thirst > 6:
        health -= 1
        print(f"You feel weak due to dehydration! Health: {health}")


    if health <= 0:
        print("You have succumbed to the harsh conditions of the desert!")
        done = True


    # Camel tiredness checks
    if camel_tiredness > 5 and not done:
        print("Your camel is getting tired and needs to rest.")
    elif camel_tiredness > 8:
        print("Your camel is dead!")
        done = True


    # Natives distance checks
    if natives_distance >= miles_traveled:
        print("The natives have caught you!")
        done = True
    elif natives_distance > miles_traveled + 15:
        print("The natives are getting close!")


    # Win condition
    if miles_traveled >= 200:
        print("You have successfully crossed the desert and escaped the natives!")
        done = True




