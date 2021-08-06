products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return products[code]

def get_property(code,property):
    return products[code][property]

def main():
    total = 0
    orders = {}
    
    while True:
        user_input = input("Input order:")
        if user_input == "/":
            break
        else:
            specific_order = user_input.split(",")
            code = specific_order[0]
            quantity = specific_order[1]
            
            if code in orders.keys():
                orders[code] += int(quantity)
            else:
                orders[code] = int(quantity)
    
    with open("receipt.txt","w") as receipttext:
        receipttext.write("""
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
""")
        for code in products.keys():
            if code in orders.keys():
                name = get_property(code,"name")
                price = get_property(code,"price")*int(orders[code])
                total += price
                receipttext.write(f"{code}\t\t{name}\t\t{orders[code]}\t\t\t\t{price}\n")
        receipttext.write(f"\nTotal:\t\t\t\t\t\t\t\t\t\t{total}\n==")

main()