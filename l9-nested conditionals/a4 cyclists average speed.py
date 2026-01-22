# Input speeds of 3 cyclists
c1 = float(input("Enter speed of Cyclist 1: "))
c2 = float(input("Enter speed of Cyclist 2: "))
c3 = float(input("Enter speed of Cyclist 3: "))

# Calculate average speed
average = (c1 + c2 + c3) / 3
print(f"\nAverage speed: {average:.2f} km/h")

# Cyclist 1
if c1 < average:
    print("Cyclist 1 is below average speed")
elif c1 > average:
    print("Cyclist 1 is above average speed")
else:
    print("Cyclist 1 is exactly at average speed")

# Cyclist 2
if c2 < average and c2 != c1:
    print("Cyclist 2 is below average speed")
elif c2 > average or c2 != c3:
    print("Cyclist 2 is above average speed")
else:
    print("Cyclist 2 is exactly at average speed")

# Cyclist 3
if c3 < average or c3 != c2:
    print("Cyclist 3 is below average speed")
elif c3 > average and c3 != c1:
    print("Cyclist 3 is above average speed")
else:
    print("Cyclist 3 is exactly at average speed")
