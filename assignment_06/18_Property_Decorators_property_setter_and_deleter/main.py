#Create a class Product with a private attribute _price. Use @property to get the price,
# @price.setter to update it, and @price.deleter to delete it.

'''Key Points:
@property makes price accessible like an attribute (p.price instead of p.get_price()).

@price.setter allows setting it with validation.

@price.deleter handles deletion logic and removes the _price attribute.

Let me know if you'd like to add default values, logging, or make it read-only.'''



class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        """Get the price."""
        return self._price

    @price.setter
    def price(self, value):
        """Set a new price."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        """Delete the price."""
        print("Deleting price...")
        del self._price

# Example:
p = Product(100)
print(p.price)      # Output: 100
p.price = 150       # Update price
print(p.price)      # Output: 150
del p.price         # Deletes the price

