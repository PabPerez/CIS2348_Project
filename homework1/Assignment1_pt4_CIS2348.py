import math
print("Enter wall height (feet):")
height = int(input())
print("Enter wall width (feet):")
width = int(input())
area = height * width
print("Wall area:", area, "square feet")

gallon = float(350)
paintNeeded = area / gallon
print("Paint needed:", '{:.2f}'.format(paintNeeded), "gallons")

cans = math.ceil(paintNeeded)
print("Cans needed:", cans, "can(s)\n")

print("Choose a color to paint the wall:")
color = str(input())
colorDict = {"red": 35, "blue": 25, "green": 23}
price = colorDict[color] * cans
print("Cost of purchasing", color, "paint: $", end="")
print(price)