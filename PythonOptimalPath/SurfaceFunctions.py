import math

# Возвращает сумму квадрата синуса первого аргумента и квадрата косинуса второго аргумента
# x - первый аргумент
# y - второй аргумент
def SinSquarePlusCosSquare(x, y):
    return math.sin(x) * math.sin(x) + math.cos(y) * math.cos(y)

# Функция Гаусса (двумерная гауссиана). 
# Описание параметров (раздел "Многомерные обобщения"): https://ru.wikipedia.org/wiki/%D0%93%D0%B0%D1%83%D1%81%D1%81%D0%BE%D0%B2%D0%B0_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F
# x, y              - точка плоскости, в которой необходимо вычислить Гауссиан
# A                 - высота колокола
# sigmaX, sigmaY    - размах колокола по оси Ox и Oy, соответственно
# x0                - сдвиг пика по оси Ox
# y0                - сдвиг пика по оси Oy
def Gaussian(x, y, A, sigmaX, sigmaY, x0, y0):
    xx = (x - x0) * (x - x0) / (2.0 * math.pow(sigmaX, 2.0))
    yy = (y - y0) * (y - y0) / (2.0 * math.pow(sigmaY, 2.0))
    return A * math.exp(-(xx + yy))

if __name__ == "__main__":
    main()