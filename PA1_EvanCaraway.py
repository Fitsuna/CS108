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

print("Grocery List:", item1,",",item2,",", item3,",", item4)


print("--------")        #section separator

#ages section
#####################
my_age = 25
your_age = 16
age_sum = my_age + your_age
age_diff = your_age - my_age
print("The sum of your age and mine is", age_sum)
print("Our age difference is", abs(age_diff))

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
num_pints = 32
print(gallons, "gallons is equivalent to", num_pints, "pints.")

pints1 = 27
num_gallons = pints1 // 8
extra_pints = ((pints1 / 8) - num_gallons)*8
print(pints1, "pints is equivalint to", int(num_gallons), "gallons and", int(extra_pints), "additional pints.")

pints1 = 105
num_gallons = pints1 // 8
extra_pints = ((pints1 / 8) - num_gallons)*8
print(pints1, "pints is equivalint to", int(num_gallons), "gallons and", int(extra_pints), "additional pints.")

