from config import CURRENCY_SYMBOL, APP_NAME

inventory_db : list[dict] = []

def format_currency(amount : float)->str:
    #Formats a floating-point number into a currency string.
    return f"{CURRENCY_SYMBOL}{amount:,.2f}"

def add_raw_product(product_id : int, name : str, price: float, stock:int)->dict:
    #Creates and inserts a product dictionary into memory with validation.
    if price < 0 :
        raise ValueError("Prices cannot be negative")
    if stock < 0:
        raise ValueError("Stocks cannot be negative")

    product = {
        "id" : product_id,
        "name" :  name,
        "price" : float(price),
        "stock" : int(stock)
    }

    inventory_db.append(product)
    return product

def calculate_total_inventory_value(inventory : list[dict])->float:
    #Calculates total monetary value across all stock items.
    total_val = 0.0
    for item in inventory:
        total_val += item["price"]*item["stock"]
    return total_val

def get_low_stock_items(inventory:list[dict], threshold : int=5)->list:
    #Returns items with stock count less than or equal to the threshold.
    return [item for item in inventory if item["stock"]<=threshold]

def update_stock_quantity(product_id : int, quantity_change : int)->bool:
    #Updates stock count for a given product ID. Handles increases and sales.
    for item in inventory_db:
        if item["id"] == product_id:
            new_stock = item["stock"]+quantity_change

            if new_stock<0:
                print(f"Error : insufficient stock for {item['name']}. Current stock is {item['stock']}")
                return False

            item['stock'] = new_stock
            return True
    print(f"Error : Product ID {product_id} not found")
    return False
