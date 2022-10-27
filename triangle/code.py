a, b, c = 10, 10, 10

def triangle_perimeter(side1=a, side2=b, side3=c):
  return side1 + side2 + side3
  
def triangle_area(side1=a, side2=b, side3=c):
  p = (side1 + side2 + side3) / 2
  return p * (p - side1) * (p - side2) * (p - side3)
