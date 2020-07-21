import pytest
from challenge_21st_July import Rectangle 

def rectange_area_test():
  for x in range(1, 10):
    for y in range(1, 10):
      rec = Rectangle(x, y)
      assert rec.area() == x*y
    