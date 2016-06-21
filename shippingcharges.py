#Jeff Masterson
#Chapter 3 #13

shipweight = int(input('Enter the weight of the product '))

if shipweight <= 2:
        print('Your product is 2 pounds or less. Your cost is $1.50')
     
elif shipweight >= 2.1 and shipweight <= 6:
    print('Your product is between 2 and 6 pounds. Your cost is $3.00')
 
elif shipweight >= 6.1 and shipweight <= 10:
    print('Your product is between 6 and 10 pounds. Your cost is $4.00')
 
elif shipweight > 10:
    print('Your product is over 10 pounds. Your cost is $4.75')
 

