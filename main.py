import sys
from services import InvalidOrderError, OutOfStockError, StoreService


def print_banner():
    print("=" * 65)
    print("         Python + SQL Store Management System        ")
    print("=" * 65)


def print_menu():
    print("\n --- MENU OPTIONS --- ")
    print("1. View all products (inventory)")
    print("2. Add New Product")
    print("3. Purchase Product")
    print("4. Exit Application")


def display_inventory(service: StoreService):
    print("\n" + "=" * 65)
    print(
        f"{'ID':<4} | {'Name':<25} | {'Price':<8} | {'Stock':<8} | {'Type'}"
    )
    print("-" * 65)

    products = service.list_inventory()
    if not products:
        print("No products in inventory.")
        print("=" * 65)
        return

    for p in products:
        # Tries 'product_type', then 'type', then checks class name or defaults to 'GENERIC'
        p_type = getattr(
            p,
            "product_type",
            getattr(p, "type", p.__class__.__name__.replace("Product", "").upper() or "GENERIC"),
        )
        print(
            f"{p.product_id:<4} | {p.name:<25} | ${p.price:<7.2f} | {p.stock:<8} | {p_type}"
        )
    print("=" * 65)


def handle_add_product(service: StoreService):
    print("\n--- ADD NEW PRODUCT ---")
    name = input("Enter Product Name : ").strip()

    try:
        price = float(input("Enter unit price ($): "))
        stock = int(input("Enter initial stock : "))
    except ValueError:
        print("Error : Price and stock must be valid numbers.")
        return  # Stop execution if input parsing fails

    print("Product Type : ")
    print(" [P] Physical (requires weight in kg)")
    print(" [D] Digital (requires download url)")
    choice = input("Select type (P/D) : ").strip().upper()

    if choice == "P":
        p_type = "PHYSICAL"
        extra_input = input("Enter weight in KG : ").strip()
    elif choice == "D":
        p_type = "DIGITAL"
        extra_input = input("Enter Download URL : ").strip()
    else:
        print("Error : Invalid Product Type")
        return

    try:
        product = service.create_product(
            name, price, stock, p_type, extra_input
        )
        print(
            f"Success! Added the product '{product.name}' with ID : {product.product_id}"
        )
    except InvalidOrderError as e:
        print(f"Validation Error : {e}")


def handle_purchase(service: StoreService):
    print("\n--- Process Purchase ---")
    try:
        product_id = int(input("Enter Product ID to buy : "))
        quantity = int(input("Enter Quantity to buy : "))
        discount = float(input("Enter discount % to apply : "))
    except ValueError:
        print("Error : Inputs must be valid numbers.")
        return

    try:
        receipt = service.process_purchase(product_id, quantity, discount)

        print("\n" + "=" * 35 + " Receipt " + "=" * 10)
        print(f"    Item : {receipt['product_name']}")
        print(f"    Quantity : {receipt['quantity']}")
        print(f"    Unit Price : ${receipt['unit_price']:.2f}")
        print(f"    Subtotal : ${receipt['subtotal']:.2f}")

        if receipt["discount_percent"] > 0:
            print(
                f"    Discount ({receipt['discount_percent']}%) : -${receipt['discount_amount']:.2f}"
            )
        print(f"    TOTAL PAID : ${receipt['final_total']:.2f}")
        print(f"    Remaining Stock : {receipt['remaining_stock']}")

    except (InvalidOrderError, OutOfStockError) as e:
        print(f"Transaction Failed : {e}")


def main():
    print_banner()
    service = StoreService()
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-4) : ").strip()

        if choice == "1":
            display_inventory(service)
        elif choice == "2":
            handle_add_product(service)
        elif choice == "3":
            handle_purchase(service)
        elif choice == "4":
            print(
                "Thank you for using Store Management System.. Shutting down"
            )
            sys.exit(0)
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()