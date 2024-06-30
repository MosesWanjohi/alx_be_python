length = int(input("Enter the size of the pattern: "))
if length <= 0:
    print("Enter a positive integer.")
row = 0

while row < length:
    for j in range(length):
        print("*", end="")
    print()
    row += 1
