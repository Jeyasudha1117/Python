class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class ECommerceSystem:
    def __init__(self):
        self.products = []
        self.cart = []

    def add_product(self, name, price, stock):
        self.products.append(Product(name, price, stock))

    def show_products(self):
        if not self.products:
            print("No products available.")
        else:
            print("\nAvailable Products:")
            for idx, product in enumerate(self.products, start=1):
                print(f"{idx}. {product.name} - ${product.price} ({product.stock} in stock)")

    def add_to_cart(self, product_index, quantity):
        if 1 <= product_index <= len(self.products):
            product = self.products[product_index - 1]
            if quantity <= product.stock:
                self.cart.append((product, quantity))
                product.stock -= quantity
                print(f"{quantity} x {product.name} added to cart.")
            else:
                print("Not enough stock available.")
        else:
            print("Invalid product selection.")

    def view_cart(self):
        if not self.cart:
            print("Cart is empty.")
        else:
            print("\nYour Cart:")
            total = 0
            for product, quantity in self.cart:
                print(f"{quantity} x {product.name} - ${product.price * quantity}")
                total += product.price * quantity
            print(f"Total: ${total}")

    def checkout(self):
        if not self.cart:
            print("Cart is empty. Add items before checkout.")
        else:
            print("\nChecking out...")
            self.view_cart()
            print("Purchase successful! Thank you for shopping.")
            self.cart.clear()


def main():
    system = ECommerceSystem()
    system.add_product("Laptop", 800, 10)
    system.add_product("Phone", 500, 15)
    system.add_product("Headphones", 50, 30)
    
    while True:
        print("\nE-Commerce System")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            system.show_products()
        elif choice == "2":
            try:
                product_index = int(input("Enter product number: "))
                quantity = int(input("Enter quantity: "))
                system.add_to_cart(product_index, quantity)
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        elif choice == "3":
            system.view_cart()
        elif choice == "4":
            system.checkout()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
