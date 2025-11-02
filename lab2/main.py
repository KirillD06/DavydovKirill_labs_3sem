from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square
from lab_python_oop.circle import Circle
import numpy as np

def main():
    N = 5
    r = Rectangle(N, N, "синий")
    c = Circle(N, "зеленый")
    s = Square(N, "красный")

    print(r)
    print(c)
    print(s)

    arr = np.array([1, 2, 3, 4, 5])
    print("Сумма элементов массива через numpy:", np.sum(arr))

if __name__ == "__main__":
    main()
