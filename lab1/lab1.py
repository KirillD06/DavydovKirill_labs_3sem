import sys
import math

def get_coef(index, prompt):
    while True:
        try:
            coef_str = sys.argv[index]
        except IndexError:
            coef_str = input(prompt)
        try:
            return float(coef_str)
        except ValueError:
            print("Некорректный ввод, попробуйте снова.")
            if index < len(sys.argv):
                sys.argv[index] = input(prompt)

def get_roots(a, b, c):
    result = []
    D = b*b - 4*a*c
    print("Дискриминант:", D)
    if D < 0:
        return result
    elif D == 0:
        y = -b / (2*a)
        if y >= 0:
            result.append(math.sqrt(y))
            if y > 0:
                result.append(-math.sqrt(y))
    else:
        sqD = math.sqrt(D)
        y1 = (-b + sqD) / (2*a)
        y2 = (-b - sqD) / (2*a)
        for y in (y1, y2):
            if y >= 0:
                result.append(math.sqrt(y))
                if y > 0:
                    result.append(-math.sqrt(y))
    return result

def main():
    a = get_coef(1, "Введите коэффициент A: ")
    b = get_coef(2, "Введите коэффициент B: ")
    c = get_coef(3, "Введите коэффициент C: ")
    roots = get_roots(a, b, c)
    if not roots:
        print("Нет действительных корней")
    else:
        print("Действительные корни:", ", ".join(map(str, roots)))

if __name__ == "__main__":
    main()
