from random import randint

class Die(object):
  def __init__(self):
    self.value = 1
  
  def roll(self):
    self.value = randint(1,6)

  def getValue(self):
    return self.value
  
  def __str__(self):
    return str(self.value)
