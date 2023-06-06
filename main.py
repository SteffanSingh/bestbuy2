# setup initial stock of inventory
import products
import store


# ***Hey this is Kapoor file

def start(store):
    while True:
        command = input("""      1. List all products in store
      2. Show total amount in store
      3. Make an order
      4. Quit
    """)
        if command == "1":
            print(store.get_all_products())
        elif command == "2":
            print(f"The total amount in store is: {store.get_total_quantity()}.")
        elif command == "3":

            try:
                count = 0
                product_list1 = store.get_all_products()

                for product in product_list1:
                    print(f"{count + 1}. {product.show()}")
                    count += 1
                order_list = order_product(product_list1, store)
                total_order = store.order(order_list)

                print(f"order made: $ {total_order}")
            except Exception as error:
                print(error, "Please enter the correct value:")

        elif command == "4":
            return True
        else:
            print("Please enter the correct command:")


def order_product(product_list1, object1):
    """the function to ask the product order and add it to the product list"""
    print("When you want to finish the order , enter empty text.")
    order_list = []

    while True:

        product_no = input("Which product # do you want ? ")
        if not product_no:
            break
        product_quantity = product_list1[int(product_no) - 1].quantity
        while True:
            product_quant = input("What amount do you want ?")
            if 0 < product_quantity < int(product_quant):
                print(f"We have only {product_quantity} in stock.  ")
                break

            elif product_quantity == 0:
                print("The product is out of stock:")
                break

            elif product_list1[int(product_no) - 1].quantity >= int(product_quant) > 0:
                order_value = (product_list1[int(product_no) - 1], int(product_quant))
                order_list.append(order_value)
                product_list1[int(product_no) - 1].quantity -= int(product_quant)
                print("product is added to list\n")
                break
    return order_list


if __name__ == "__main__":
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)
