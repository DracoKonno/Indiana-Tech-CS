#Problem 1

def add_to_order(order, item_name, quantity, price_per_item):
    if quantity and price_per_item > 0:
        order [item_name] = (quantity, price_per_item) if item_name not in order else order.update(quantity)
    else:
        print("Error: Values can not be negative")

def remove_from_order(order, item_name):
    pass

def calculate_bill(order, tax_rate):
    pass

if __name__ == "__main__":
    order = {}
    order = {'burger': (2, 8.99)}

    #test cases
    print(add_to_order(order, "Burger", 2, 8.99))
    print(add_to_order(order, "Fries", -1, 3.50))
    print(add_to_order(order, "Drink", 2, 2.99))
    
    print(f"Order; {order}")
    
    