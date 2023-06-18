# setup initial stock of inventory
import products
import store
import promotions


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
                    if product.name == "Windows License":
                        product.quantity = 0
                    print(f"{count + 1}. {product.show()}")
                    count += 1
                order_list = order_product(product_list1, store)
                total_order = store.order(order_list)

                print(f"order made: $ {total_order}")
            except ValueError:
                print("Please enter the correct input:")

        elif command == "4":
            return True

        else:
            print("Please enter the correct command:")


def order_product(product_list1, object1):
    """the function to ask the product order and add it to the product list"""
    print("When you want to finish the order , enter empty text.")
    order_list = []

    while True:

        try:
            product_no = input("Which product # do you want ? ")




            if not product_no:
                break
            while int(product_no) > len(product_list1):
                print(f"There are only  {len(product_list1)} products. ")
                print(f"Enter the value less than {len(product_list1)}\n***")
                product_no = input(f"""Which product # do you want ? """)
            product_quantity = product_list1[int(product_no) - 1].quantity

            product1 = product_list1[int(product_no) - 1]
            while True:

                product_quant = input("What amount do you want ?")
                while int(product_quant) < 0:
                    product_quant = input("Please enter the valid quantity in positive integer:  ")

                if 0 < product_quantity < int(product_quant):
                    print(f"We have only {product_quantity} in stock.  ")
                    break

                elif product_quantity == 0 and product1.name != "Windows License":
                    print("The product is out of stock:")
                    break

                elif product1.name == "Shipping" and int(product_quant) > 1:
                    print(" Shipping cant be more than 1")
                    break


                elif product1.quantity >= int(product_quant) > 0 or product1.name == "Windows License":
                    if product1.name == "Shipping" and (product1, 1) in order_list:
                        print("Shipping can be added only once")
                        break
                    else:
                        order_value = (product1, int(product_quant))
                        order_list.append(order_value)

                        product1.quantity -= int(product_quant)
                        print("product is added to list\n")
                        break

        except ValueError as e:
            print("Please enter a valid input: ")

    return order_list


if __name__ == "__main__":
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)

    product_list[1].set_promotion(third_one_free)

    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)
    start(best_buy)
