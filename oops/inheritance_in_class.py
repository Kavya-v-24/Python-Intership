class human:
  def __init__(self,hobby,food):
    self.fav_hobby=hobby
    self.fav_food=food

  def display_info(self):
    print(f"she plays {self.fav_hobby}, and she likes {self.fav_food}")

class ruksar(human):
  def __init__(self,hobby,food,language): 
      super().__init__(hobby,food)
      self.fav_language=language

  def display_info(self):
      super().display_info()
      print(f"language she speaks {self.fav_language}")

user=ruksar("games","biryani","tamil")
user.display_info()