from store import Store
from products import Product

Coops = Store(name="Coops")

skates = Product('Skates',800,'Hockey')
stick = Product('Stick',300,'Hockey')

Coops.add_product(skates)
Coops.add_product(stick)

skates.print_info()
stick.print_info()

# Coops.sell_product(0)

Coops.set_clearance('Hockey', .50)
print('*'*50)
skates.print_info()
stick.print_info()