# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:33:06 2024

@author: m171548
"""

import random
import matplotlib.pyplot as plt

def Graph(value) -> None:
    y = [x for x in range(len(value))]
    plt.title("Projected Investment Growth")
    plt.xlabel("Number of Years")
    plt.ylabel("Account Balance")
    plt.plot(y, value)
    plt.grid()
    plt.savefig("Roth Forecast.jpg")
    plt.show()
    plt.close()

def Main() -> None:
    # Set starting variables
    value = []
    age = int(input("Current Age: "))
    starting_value = float(input("Starting Roth IRA Value: "))
    value.append(starting_value)
    contribution = float(input("Contributions per year ($7000 Limit): "))
    i = 0
    
    # iterate until you have your first million dollars
    while starting_value < 1000000:
        if age >= 50 and contribution != 8000:
            contribution = float(8000) 
        annual_return = round(random.uniform(1.07,1.10),2)
        i+=1
        age+=1
        starting_value = (starting_value*annual_return) + contribution
        value.append(starting_value)
    print("\n"+ str(i), "years")
    print(age, "years old")
    print("$"+str(round(starting_value,2)), "\n")

    # iterate until you are of retiring age.
    while age < 65:
        if age >= 50 and contribution != 8000:
            contribution = 8000  
        annual_return = round(random.uniform(1.07,1.10),2)
        age+=1
        i+=1
        starting_value = (starting_value*annual_return) + contribution
        value.append(starting_value)
    print(i, "years")
    print(age, "years old")
    print("$"+str(round(starting_value,2)), "\n")
    
    # iterate one more year without contribution
    annual_return = round(random.uniform(1.07,1.10),2)
    i+=1
    age+=1
    final_value = (starting_value*annual_return)
    value.append(final_value)
    print(i, "years")
    print(age, "years old")
    print("$",round(final_value,2))
    print("You made $" + str(round(final_value-starting_value,2)) + " without contributions after you retired.\n")
    
    Graph(value)
    
if __name__=="__main__":
    Main()