import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.product import DigitalProduct, PhysicalProduct, Product
from repositories.product_repository import ProductRepository

class OutOfStockError(Exception):
    pass

class InvalidOrderError(Exception):
    pass

class StoreService:
    def __init__(self, product_repo : ProductRepository | None = None):
        self.repo = product_repo or ProductRepository()

    def create_product(self, name : str, price : float, stock : int, p_type : str, extra_param : str | float) -> Product:
        if price <= 0 :
            raise InvalidOrderError("Product price must be greater than $0.00.")

        if stock < 0 :
            raise InvalidOrderError("Initial stock cannot be negative.")

        normalized_type = p_type.strip().upper()

        if normalized_type == "PHYSICAL":
            weight = float(extra_param)
            if weight <= 0:
                raise InvalidOrderError("Physical product weight must be positive.")
            product = PhysicalProduct(name = name, price=price, stock=stock, weight_kg=weight)

        elif normalized_type == "DIGITAL":
            url = str(extra_param)
            if not url:
                raise InvalidOrderError("Digital Products require a download url.")
            product = DigitalProduct(name = name, price=price, stock=stock, download_url=url)

        else : 
            raise InvalidOrderError("Unsupported product type")

        self.repo.add_product(product)
        return product

    def process_purchase( self, product_id : int, quantity : int, discount_percent : float = 0.0)->dict:
        if quantity <= 0:
            raise InvalidOrderError("Purchase wuantity must be atleast 1")
        if not(0.0 <= discount_percent <= 100.0):
            raise InvalidOrderError("Discount must be between 0 and 100.")

        product = self.repo.get_by_id(product_id)
        if not product:
            raise InvalidOrderError(f"Product with ID {product_id} does not exist.")

        if product.stock < quantity :
            raise OutOfStockError(f"Cannot fulfill order for {quantity} unit(s) . Only {product.stock}")

        unit_price = product.price
        subtotal = unit_price*quantity
        discount_amount = subtotal * (discount_percent/100.0)
        final_total = subtotal - discount_amount

        new_stock = product.stock - quantity
        self.repo.update_stock(product_id, new_stock)
        product.stock - new_stock

        return {
            "product_id" : product_id,
            "product_name" : product.name,
            "quantity": quantity,
            "unit_price": round(unit_price, 2),
            "subtotal": round(subtotal, 2),
            "discount_percent": discount_percent,
            "discount_amount": round(discount_amount, 2),
            "final_total": round(final_total, 2),
            "remaining_stock": new_stock,
        }

    def list_inventory(self)-> list[Product]:
        return self.repo.get_all()


if __name__ == "__main__":
    print("Testing StoreService Business Logic...\n")
    service = StoreService()

    # 1. Add Products through Service Layer
    p1 = service.create_product("Logitech MX Master 3S", 99.99, 10, "PHYSICAL", 0.35)
    p2 = service.create_product("FastAPI Complete Masterclass", 29.99, 50, "DIGITAL", "https://dcodeit.com/fastapi")

    print(f"Created Physical Product: ID {p1.product_id} - {p1.name}")
    print(f"Created Digital Product:  ID {p2.product_id} - {p2.name}")

    # 2. Process Successful Purchase with 10% Discount
    print("\n--- Processing Order 1 ---")
    receipt = service.process_purchase(product_id=p1.product_id, quantity=2, discount_percent=10.0)
    print(f"Receipt for '{receipt['product_name']}':")
    print(f"  Qty: {receipt['quantity']} @ ${receipt['unit_price']} each")
    print(f"  Subtotal: ${receipt['subtotal']}")
    print(f"  Discount ({receipt['discount_percent']}%): -${receipt['discount_amount']}")
    print(f"  Final Total: ${receipt['final_total']}")
    print(f"  Stock Left: {receipt['remaining_stock']}")

    # 3. Test Business Logic Error Handling (Out of Stock)
    print("\n--- Testing Stock Boundary Validation ---")
    try:
        service.process_purchase(product_id=p1.product_id, quantity=50)
    except OutOfStockError as e:
        print(f"Handled Expected Error: {e}")