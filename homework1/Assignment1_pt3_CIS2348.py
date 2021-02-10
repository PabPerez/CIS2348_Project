print("Enter amount of lemon juice (in cups):")
lemonJuice = int(input())

print("Enter amount of water (in cups):")
water = int(input())

print("Enter amount of agave nectar (in cups):")
agave = float(input())

print("How many servings does this make?\n")
servings = int(input())

print("Lemonade ingredients - yields", '{:.2f}'.format(servings), "servings")
print('{:.2f}'.format(lemonJuice), "cup(s) lemon juice")
print('{:.2f}'.format(water), "cup(s) water")
print('{:.2f}'.format(agave), "cup(s) agave nectar\n")

servings1 = int(input())
mult = servings1 / servings

lemonJuice1 = lemonJuice * mult
water1 = water * mult
agave1 = agave * mult
print("How many servings would you like to make?\n")
print("Lemonade ingredients - yields", '{:.2f}'.format(servings1), "servings")
print('{:.2f}'.format(lemonJuice1), "cup(s) lemon juice")
print('{:.2f}'.format(water1), "cup(s) water")
print('{:.2f}'.format(agave1), "cup(s) agave nectar\n")

print("Lemonade ingredients - yields", '{:.2f}'.format(servings1), "servings")
lemong = lemonJuice1 / 16
waterg = water1 / 16
agaveg = agave1 / 16

print('{:.2f}'.format(lemong), "gallon(s) lemon juice")
print('{:.2f}'.format(waterg), "gallon(s) water")
print('{:.2f}'.format(agaveg), "gallon(s) agave nectar")