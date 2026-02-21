def invoice_total(*array):
    total = sum(array)
    return total
n = int(input("Enter no of entries : "))
arr = []
for i in range(n):
    val = int(input(f"Enter value {i+1}: "))
    arr.append(val)

print(f"Total = {invoice_total(*arr)}")
