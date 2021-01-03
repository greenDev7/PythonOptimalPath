import math
from Point3D import Point3D
from SurfaceFunctions import SinSquarePlusCosSquare as SC, Gaussian as G

def GetSquareOfDistance(point, testedPoint, dy):
    """Возвращает относительный квадрат расстояния до проверяемой точки"""
    return math.pow(point.z - testedPoint.z, 2.0) + testedPoint.PositionalParameter + dy * dy

def GetTangentSquare(point, testedPoint, dx, dy):
    """Возвращает квадрат тангенса угла между точками"""
    return math.pow(point.z - testedPoint.z, 2.0) / (dx ** 2 + testedPoint.PositionalParameter * dy * dy)
    
def main():
    
    # Формируем матрицу 3 на 4 как массив массивов, содержащей 3 массива в каждом из котором по 4 элемента
    # и инициализируем все элементы матрицы нулевыми значениями
    n = 3
    m = 4
    Matrix = [[0 for x in range(m)] for y in range(n)]

    for i in range(n):
        for j in range(m):
            Matrix[i][j] = 'sdf'

    print(SC(3.14159265358979, 0.0))
    print(G(1, 2, 1, 1, 1, 1, 1))
    
if __name__ == "__main__":
    main()
