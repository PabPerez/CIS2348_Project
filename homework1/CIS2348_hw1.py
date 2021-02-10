print("Birthday Calculator")
print("Enter current date by month, day, and year; starting with month")

print("Current Day")
print("Input Month (use #'s not words)")
currentM = int(input())
print("Month:", currentM)

print("Input Day (use #'s not words)")
currentD = int(input())
print("Day:", currentD)

print("Input Year (use #'s not words)")
currentY = int(input())
print("Year:", currentY)

print("Birthday Date")
print("Input Birthday Month (use #'s not words)")
bdayM = int(input())
print("Month:", bdayM)

print("Input Birthday Day (use #'s not words)")
bdayD = int(input())
print("Day:", bdayD)

print("Input Birthday Year (use #'s not words)")
bdayY = int(input())
print("Year:", bdayY)

if (currentM == bdayM) and (currentD == bdayD) and (currentY == bdayY):
    print("Happy Birthday!")
else:
    ageY = currentY - bdayY
    print("You are", ageY, "years old.")
