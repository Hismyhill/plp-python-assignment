def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (discount_percent / 100)
    else: return price

price = int(input("Enter the price: ") )   
discount_percent = int(input("Enter the discount: ") )   
print(calculate_discount(price, discount_percent))
