sec=int(input("Please enter a number to represent seconds: "))
hours=sec//3600
minutes=sec%3600//60
secs=sec%3600%60
print("Hours:",hours,"\nMinutes:",minutes,"\nSeconds:",secs)