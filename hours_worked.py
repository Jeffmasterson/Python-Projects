#Jeff Masterson
#hours worked

#Initialize the accumulator.
total = 0

# Get the hours worked for each day.
for day in range (1, 6):
    print ('How many hours did you work on day', day, 'of this week? ')
    hours = int(input())
    total = total + hours

#display the total hours worked.
print ('You have worked a total of ', total, 'hours this week.')     

