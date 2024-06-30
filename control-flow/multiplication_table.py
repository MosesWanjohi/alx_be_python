number = int(input("Enter a number you want to see its multiplication table: "))
Z = "product"
X = number
for Y in range(1, 11):
    Z = X * Y
    print()
    print(f"{X} x {Y} = {Z}", end="\t")
print() 
