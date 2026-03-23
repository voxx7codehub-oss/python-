weight = int (input("Enter input : "))
if weight <= 0 or weight > 7000:
    print("INVALID INPUT")
elif weight == 0:
    print("TIME ESTIMATED: 0 MINUTES")
elif weight == 2000:
    print("TIME ESTIMATED: 25 MINUTES")
elif weight >2000 and weight <= 4000:
    print("TIME ESTIMATED: 35 MINUTES")
elif weight >4000 and weight <= 7000:
    print("TIME ESTIMATED: 45 MINUTES")
else:
    print("OVERLOAD")
