'''
-------------------------------------------------------------------------------
Name: Evan Caraway
Assignment: PA1
Due Date: Sept 2nd, 2024	
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by the professor and class syllabus.
-------------------------------------------------------------------------------
Comments: N/A
-------------------------------------------------------------------------------
'''

print("This is my first program.")
print("--------")        #section separator

#grocery list section
#####################
item1 = "milk"
item2 = "oats"
item3 = "dish soap"
item4 = "peanut butter"
print("Grocery List:", item1, item2, item3, item4)


print("--------")        #section separator

#ages section
#####################
myAge = 25
yourAge = 16
ageSum = myAge + yourAge
ageDiff = abs(yourAge - myAge)
print("The sum of your age and mine is", ageSum)
print("Our age difference is", ageDiff)

print("--------")        #section separator

# temperatures section
######################
temp1 = 88.5
temp2 = 53.9
temp3 = 66.3
temp4 = 73.94
numTemps = 4
avgTemp = (temp1 + temp2 + temp3 + temp4)/numTemps
print("The average temperature is:", avgTemp)

print("--------")        #section separator

# pints and gallons
#######################
#NOTE: There are 4 quarts in a gallon
#      There are 8 pints in a gallon


gallons = 4
numPints = gallons * 8
print(gallons, "gallons is equivalent to", numPints, "pints.")

pintsOne = 27
numGallons = pintsOne // 8
extraPints = ((pintsOne / 8) - numGallons)*8
print(pintsOne, "pints is equivalint to", int(numGallons), "gallons and", int(extraPints), "additional pints.")

pintsOne = 105
numGallons = pintsOne // 8
extraPints = ((pintsOne / 8) - numGallons)*8
print(pintsOne, "pints is equivalint to", int(numGallons), "gallons and", int(extraPints), "additional pints.")
