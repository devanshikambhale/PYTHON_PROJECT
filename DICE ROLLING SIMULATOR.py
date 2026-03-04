# Dice Rolling Simulator.
# This program is used to roll dice using random numbers.

import random   # we are importing random module to get random numbers

# this function will roll the dice
def roll_dice(number_of_dice):   # number_of_dice means how many dice we want to roll
    results = []   # here we create an empty list to store dice numbers
    
    for i in range(number_of_dice):   # this loop will run based on user input
        value = random.randint(1, 6)   # this will generate number between 1 and 6
        results.append(value)   # adding the number into the list
    
    return results   # sending the list back to main function


# main function starts here
def main():
    print("🎲 Dice Rolling Simulator 🎲")   # printing the heading
    
    while True:   # loop will keep running until user stops it
        try:
            # taking input from user and converting into integer
            dice_count = int(input("Enter number of dice to roll: "))
            
            if dice_count <= 0:   # checking if user entered 0 or negative number
                print("Please enter a positive number.")   # showing message
                continue   # again asking for input
            
            result = roll_dice(dice_count)   # calling the roll_dice function
            
            print("----------------------")
            print("You rolled:", result)   # printing dice values
            print("Total Score=", sum(result))   # printing total of all dice values
            print("----------------------")
        except ValueError:   # if user enters text instead of number
            print("Invalid input!! Please enter a valid number.")   # showing error
        
        # asking user if they want to roll again
        choice = input("would you like to roll again? (yaa/nope): ").lower()
        
        if choice != "yaa":   # if user does not type yes
            print("Thank you for using Dice Simulator!!")   # ending message
            break   # stopping the loop


# calling main function to start the program
main()