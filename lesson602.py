class Vehicle:
  def __init__(self, owner, model, engine_power, color):
    self.owner = owner
    self.__model = model
    self.__engine_power = engine_power
    self.__color = color
    Vehicle.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

  def get_model(self):
    return f"Модель: {self.__model}"

  def get_horsepower(self):
    return f"Мощность двигателя: {self.__engine_power}"

  def get_color(self):
    return f"Цвет: {self.__color}"

  def print_info(self):
    return (
        f"{self.get_model()}\n"
        f"{self.get_horsepower()}\n"
        f"{self.get_color()}\n"
        f"Владелец: {self.owner}"
    )

  def set_color(self, new_color):
    if new_color.lower() in [color.lower() for color in Vehicle.__COLOR_VARIANTS]:
      self.__color = new_color
    else:
      print(f"Нельзя сменить цвет на {new_color}")
    
class Sedan(Vehicle):
  def __init__(self, owner, model, engine_power, color):
    super().__init__(owner, model, engine_power, color)
    Sedan.__PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
print(vehicle1.print_info())
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
print(vehicle1.print_info())

