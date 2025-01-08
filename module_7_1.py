class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def get_products(self):
        __file_name = 'products.txt'
        file = open(__file_name, 'r')
        global a
        a = str(file.read())
        file.close()
        return a

    def add(self, *products):
        for Product in products:
            if str(Product) not in self.get_products():
                __file_name = 'products.txt'
                file = open(__file_name, 'a+')
                file.write(f'\n{str(Product)}')
                file.close()
            else:
                print(f'Продукт {Product.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())