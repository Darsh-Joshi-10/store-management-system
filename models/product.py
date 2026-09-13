from abc import ABC, abstractmethod

class Product(ABC):
    """Abstract Base Class representing a core product entity."""

    def __init__(self, name: str, price: float, stock: int, product_id: int | None = None):
        self.product_id = product_id
        self.name = name
        self._price = 0.0
        self._stock = 0

        self.price = price
        self.stock = stock  # 1. Fixed typo (was self.stocks)

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Price can't be negative")
        self._price = float(value)

    @property
    def stock(self) -> int:  # 2. Fixed return type hint to int
        return self._stock
    
    @stock.setter
    def stock(self, value: int) -> None:  # 3. Fixed method name (was def price)
        if value < 0:
            raise ValueError("Stock can't be negative")
        self._stock = int(value)
    
    def calculate_total_value(self) -> float:
        return self._price * self._stock

    @abstractmethod
    def get_details(self) -> str:
        pass

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(id={self.product_id}, name='{self.name}', price={self._price}, stock={self._stock})>"


class PhysicalProduct(Product):
    """Represents physical inventory items requiring weight/shipping tracking."""

    def __init__(self, name: str, price: float, stock: int, weight_kg: float = 0.0, product_id: int | None = None):
        super().__init__(name, price, stock, product_id)
        self.weight_kg = weight_kg

    def get_details(self) -> str:
        return f"[Physical] {self.name} | Price: ${self.price:,.2f} | Stock: {self.stock} | Weight: {self.weight_kg}kg"


class DigitalProduct(Product):
    """Represents digital items with digital download keys or licenses."""

    def __init__(self, name: str, price: float, stock: int, download_url: str = "", product_id: int | None = None):
        super().__init__(name, price, stock, product_id)
        self.download_url = download_url

    def get_details(self) -> str:
        # 4. Fixed tag to [Digital] and removed trailing 'kg'
        return f"[Digital] {self.name} | Price: ${self.price:,.2f} | Stock: {self.stock} | URL: {self.download_url}"


if __name__ == "__main__":
    print("Testing Domain Models...\n")

    # Instantiating polymorphic subclasses
    laptop = PhysicalProduct("MacBook Pro 16", 2499.99, 5, weight_kg=2.1, product_id=1)
    e_book = DigitalProduct("Python Design Patterns", 29.99, 100, download_url="https://dcodeit.com/ebook", product_id=2)

    print(laptop.get_details())
    print(e_book.get_details())
    print(f"Laptop Valuation: ${laptop.calculate_total_value():,.2f}")

    # Testing validation catch
    try:
        laptop.price = -500  # Should trigger ValueError
    except ValueError as e:
        print(f"\nSuccessfully caught invalid operation: {e}")