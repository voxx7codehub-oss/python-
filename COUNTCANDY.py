N = int(input("Enter maximum count of caandies: "))
k = int(input("Enter minimum count of caandies: "))
CANDIES = N
while True:
    order = int(input("Enter candies to purchase: "))
    if order <= 0 or order > CANDIES:
        print(" INVALID INPUT ")
        print("NUMBER OF CANDIES LEFT : ",CANDIES)
    else:
        CANDIES -= order
        print("NUMBER OF CANDIES SOLD :" ,order)
        print("NUMBER OF CANDIES AVAILBLE :",CANDIES)
    if CANDIES <= k:
       CANDIES = N
