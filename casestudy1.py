# Grocery Store Billing System
# MUKESH KUMAR
# 202501100700200
total = 0
discount = 0

item_count = int(input("Enter number of unique items: "))

for i in range(1, item_count + 1):
    print(f"\nItem {i}")
    item_quantity = int(input(f"Enter quantity of item {i}: "))
    price = float(input(f"Enter price of item {i}: "))
    
    total += price * item_quantity 


if total > 100:
    discount = total * 0.10
    new_total = total - discount
else:
    new_total = total  

print("\nTotal before discount:", total, "Rs")
print("Discount:", discount, "Rs")
print("Total after discount:", new_total, "Rs")
print("Total saving:", discount, "Rs")
