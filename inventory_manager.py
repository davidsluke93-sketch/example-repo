#inventory app Code

#step 1:Check for stock

stock_name="Playstation 5" 
stock_quantity= 5

#if function
if stock_quantity<10:
    print(stock_name,"Stock is low restock needed!")
else:
    print(stock_name,"Restock is not needed")

#step 2:Evaluate stock levels

item_name = "Laptop"
stock_quantity = 5

if stock_quantity < 10:
    print(item_name, "is low in stock. Restock needed!")
else:
    print(item_name, "has sufficient stock.")

 # Step 3: Categorise stock levels

item_name = "Playstation 5"
stock_quantity = 20

if stock_quantity < 10:
    print(item_name, "is low in stock. Restock needed!")

elif stock_quantity <= 30:
    print(item_name, "has sufficient stock.")

else:
    print(item_name, "is overstocked!")   


# Step 4: Create a item dictionary

stock_items = {
    "Item A": 10,
    "Item B": 20,
    "Item C": 5
}

# Loop through each item and check stock

for item, quantity in stock_items.items():

    if quantity < 10:
        print(item, "Low stock. Restock needed!")

    elif quantity <= 30:
        print(item, "Sufficient stock.")

    else:
        print(item, "Overstocked!")


# Step 5: Restock until stock reaches target of30

stock_quantity = 5
target_stock = 30

while stock_quantity < target_stock:
    stock_quantity += 5
    print("Current stock:", stock_quantity)

print("Restocking complete!")        


# Step 6: Use break and continue

stock_items = {
    "Item A": 10,
    "Item B": 30,
    "Item C": 5
}

target_stock = 30
max_stock = 50

for item, quantity in stock_items.items():

    if quantity >= target_stock:
        print(item, "has enough stock. Skipping!")
        continue

    while quantity < target_stock:
        quantity += 5

        if quantity > max_stock:
            print(item, "exceeded maximum stock!")
            break

        print(item, "Current stock:", quantity)

    stock_items[item] = quantity

print("Restocking process complete!")

  # Step 7: Create a placeholder function

def send_alert(item_name):
    pass

# Check low stock
stock_quantity = 5
item_name = "Item C"

if stock_quantity < 10:
    print(item_name, "is low in stock!")
    send_alert(item_name)