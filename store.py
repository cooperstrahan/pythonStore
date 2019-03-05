from products import Product

class Store:
    def __init__(self, name="", products=[]):
        self.name = name
        self.products = products
    
    def add_product(self, new_product):
        self.products.append(new_product)

    # remove the product from the store's list of products given the id 
    # (assume id is the index of the product in the list) and print its info.
    def sell_product(self, id):
        print("Product Name:", self.products[id].name)
        print("price", self.products[id].price,)
        print("category", self.products[id].category)
        self.products.pop(id)
        
    # increases the price of each product by the percent_increase given 
    # (use the method you wrote in the Product class!)
    def inflation(self, percent_increase):
        for p in self.products:
            p.update_price(percent_increase, True)
    
    # updates all the products matching the given category by reducing the price 
    # by the percent_discount given (use the method you wrote in the Product class!)
    def set_clearance(self, category, percent_discount):
        for p in self.products:
            if p.category == category:
                p.update_price(percent_discount, False)
