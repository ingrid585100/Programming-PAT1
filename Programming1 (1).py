def log_inventory():
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity received: "))
    supplier = input("Enter supplier name: ")
    cost_per_unit = float(input("Enter cost per unit (R): "))

    total_cost = quantity * cost_per_unit
    large_order = " (Large Order)" if total_cost > 500 else ""

    log_entry = f"Product: {product_name}, Quantity: {quantity}, Supplier: {supplier}, Total Cost: R{total_cost:.2f}{large_order}\n"

    with open("inventory_log.txt", "a") as file:
        file.write(log_entry)

    print(f"Binary representation: {bin(int(total_cost))[2:]}")

log_inventory()