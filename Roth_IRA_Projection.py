# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:33:06 2024

@author: m171548
"""

import random
import matplotlib.pyplot as plt

def Graph(value, contribution) -> None:
    y = [x for x in range(len(value))]
    plt.title("Projected Investment Growth")
    plt.xlabel("Number of Years")
    plt.ylabel("Account Balance")
    plt.plot(y, value, label = "Value")
    plt.plot(y, contribution, label = "Contribution")
    plt.grid()
    plt.legend()
    plt.savefig("Roth Forecast.jpg")
    plt.show()
    plt.close()

def Main() -> None:
    # Set starting variables
    value = []
    contribution_list = []
    contribution_value = []
    age = int(input("Current Age: "))
    starting_value = float(input("Starting Roth IRA Value: "))
    value.append(starting_value)
    deposit_value = float(input("Starting Deposit Value: "))
    contribution = float(input("Contributions per year ($7500 Limit): "))
    contribution_list.append(deposit_value)
    contribution_value.append(deposit_value)
    i = 0
    check = 0
    
    # iterate until you have your first million dollars
    while starting_value < 1000000:
        if age >= 50 and contribution != 8600:
            contribution = float(8600) 
        if contribution_value[len(contribution_value)-1]<(value[len(value)-1]-contribution_value[len(contribution_value)-1]) and check == 0:
            check = 1
            print("\n%0.0f years old when returns are greater than contributions." % age)
        
        annual_return = round(random.uniform(1.07,1.10),2)
        i+=1
        age+=1
        starting_value = (starting_value*annual_return) + contribution
        value.append(starting_value)
        contribution_list.append(contribution)
        contribution_value.append(sum(contribution_list))
    print("\n"+ str(i), "years")
    print(age, "years old")
    print("$"+str(round(starting_value,2)), "\n")

    # iterate until you are of retiring age.
    while age < 65:
        if age >= 50 and contribution != 8600:
            contribution = 8600  
        annual_return = round(random.uniform(1.07,1.10), 2)
        age+=1
        i+=1
        starting_value = (starting_value*annual_return) + contribution
        value.append(starting_value)
        contribution_list.append(contribution)
        contribution_value.append(sum(contribution_list))
    print(i, "years")
    print(age, "years old")
    print("$"+str(round(starting_value,2)), "\n")
    
    # iterate one more year without contribution
    annual_return = round(random.uniform(1.07,1.10),2)
    i+=1
    age+=1
    final_value = (starting_value*annual_return)
    value.append(final_value)
    contribution_list.append(0)
    contribution_value.append(sum(contribution_list))
    print(i, "years")
    print(age, "years old")
    print("$",round(final_value,2))
    print("You made $" + str(round(final_value-starting_value,2)) + " without contributions after you retired.\n")
    
    Graph(value, contribution_value)
    
if __name__=="__main__":
    Main()