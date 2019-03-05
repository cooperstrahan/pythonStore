class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent_changed, is_increased):
        if is_increased == True:
            self.price *= (1+percent_changed)
        elif is_increased == False:
            self.price *= (1-percent_changed)
        return self
    
    def print_info(self):
        print("Product Name:",self.name)
        print("Price:",self.price)
        print("Category:",self.category)
        return self
