a = int(input("Enter the day of the week (number): "))
if a==6 or a==7:
    print("weekend")
elif 0 > a < 8:
    print("It's not a day of the week")
else:
    print("weekday")
print("Thank you for participating in the survey:)")