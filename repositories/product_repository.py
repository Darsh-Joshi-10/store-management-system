import os
import sys

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) )

from database.db_handler import DatabaseHandler
from models.product import Product, PhysicalProduct, DigitalProduct


class ProductRepository:

    def __init__(self, db_handler : DatabaseHandler | None = None):
        self.db = db_handler or DatabaseHandler()

    def _map_row_to_product(self, row:tuple)->Product:

        p_id, name, price, stock, p_type, extra_info, _ = row

        if p_type.upper() == "PHYSICAL":
            weight = float(extra_info) if extra_info else 0.0
            return PhysicalProduct(name=name, price=price, stock=stock, weight_kg=weight, product_id=p_id)

        elif p_type.upper() == "DIGITAL":
            url = extra_info or ""
            return DigitalProduct(name=name, price=price, stock=stock, download_url=url, product_id=p_id)

        else:
            raise ValueError(f"Unknown product type '{p_type}' found in database.")

    def add_product(self, product : Product)->int:

        if isinstance(product, PhysicalProduct):
            p_type = "PHYSICAL"
            extra_info = str(product.weight_kg)

        elif isinstance(product, DigitalProduct):
                p_type = "DIGITAL"
                extra_info = str(product.download_url)

        else:
            raise TypeError("Unsupported product subclass type")

        query = """
                INSERT INTO products (name, price, stock, product_type, extra_info)
                VALUES (?, ?, ?, ?, ?)
                """

        params = (product.name, product.price, product.stock, p_type, extra_info)

        new_id = self.db.execute_query(query, params)

        product.product_id = new_id

        return new_id

    def get_all(self)->list[Product]:
        query = "SELECT * FROM products"
        rows = self.db.fetch_all(query)
        return [self._map_row_to_product(row) for row in rows]

    def get_by_id(self, product_id)-> Product |None:
        query = "SELECT * from products where id = ?"
        row = self.db.fetch_one(query, (product_id, ))
        if row :
            return self._map_row_to_product(row)
        return None



    def update_stock(self, product_id : int, new_stock : int)-> bool : 
        if new_stock<0:
            raise ValueError("Stock value cant be lower than 0")

        query = "UPDATE products SET stock = ? WHERE id = ?"
        self.db.execute_query(query, (new_stock, product_id))
        return True

    def delete(self, product_id : int)-> bool:
        query = "DELETE FROM products WHERE id = ?"
        self.db.execute_query(query, (product_id,))
        return True