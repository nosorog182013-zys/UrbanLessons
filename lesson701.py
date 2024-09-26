#Домашнее задание по теме "Режимы открытия файлов"
class Product:
  def __init__(self, name, weight, category):
    self.name = name
    self.weight = weight
    self.category = category

  def __str__(self):
    return f"{self.name}, {self.weight}, {self.category}"

class Shop:
  def __init__(self, __file_name):
    self.__file_name = "products.txt"
    self.__products = self.load_products()

  def load_products(self):
    products = []
    try:      
      with open(self.__file_name, 'r') as f:
        for line in f:
          name, weight, category = line.strip().split(',')
          products.append(Product(name, float(weight), category))
    except FileNotFoundError:
      pass
    return products
    
  def get_products(self):
    products_string = ""
    with open(self.__file_name, 'r') as file:
      content = file.read()
      lines = content.splitlines()
      for line in lines:
        name, weight, category = line.split(',')
        product = f"{name}, {weight}, {category}\n"
        products_string += product
    return products_string

  def add(self, *products):
    for product in products:
      product_exists = False
      with open(self.__file_name, 'r') as f:
        for line in f:
          if str(product) == line.strip():
            product_exists = True
            break
      if product_exists:
        print(f"Продукт {str(product)} уже есть в магазине.")
      else:
        self.__products.append(product)
        self.save_products()
         
  def save_products(self):
    with open(self.__file_name, 'w') as f:
      for product in self.__products:
        f.write(f"{product}\n")
      
s1 = Shop("products.txt")
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())

