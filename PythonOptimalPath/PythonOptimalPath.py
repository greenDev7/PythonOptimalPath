import math
from Point3D import Point3D
from SurfaceFunctions import SinSquarePlusCosSquare as SC, Gaussian as G

def GetSquareOfDistance(point, testedPoint, dy):
    """Возвращает относительный квадрат расстояния до проверяемой точки"""
    return math.pow(point.z - testedPoint.z, 2.0) + testedPoint.PositionalParameter * dy * dy

def GetTangentSquare(point, testedPoint, dx, dy):
    """Возвращает квадрат тангенса угла между точками"""
    return math.pow(point.z - testedPoint.z, 2.0) / (dx * dx + testedPoint.PositionalParameter * dy * dy)
    
def main():
    
    # Шаги сетки по осям Ox, Oy
    dx, dy = 0.1, 0.1

    # Количество узлов сетки по осям Ox, Oy
    N = 100
    M = 30

    # Формируем матрицу N на M как массив массивов и инициализируем нулевыми значениями
    grid = [[0 for x in range(M)] for y in range(N)]
    
    # Формируем карту местности с помощью функции, задающей двумерную поверхность
    for i in range(N):
        for j in range(M):
            grid[i][j] = SC(i * dx, j * dy)

    # Координаты конца неизвестного маршрута, который необходимо продолжить
    N_ = 98
    M_ = 16   
    
    # Первая точка маршрута
    currentOptimalPoint = Point3D(N_, M_, grid[N_][M_], 0)
    # Временный список и список для хранения искомого оптимального пути
    tempPnts, optimalPath = [], []

    # Добавляем в список с искомым маршрутом первую точку, которая уже известна
    optimalPath.append(currentOptimalPoint)

    # Основной цикл поиска оптимального пути
    for i in reversed(range(N_)):
        M_ = currentOptimalPoint.M

        if (M_ == 0):
            tempPnts.append(Point3D(i, 0, grid[i][0], 0))
            tempPnts.append(Point3D(i, 1, grid[i][1], 1))
        elif (M_ == M - 1):
            tempPnts.append(Point3D(i, M - 1, grid[i][M - 1], 0))
            tempPnts.append(Point3D(i, M - 2, grid[i][M - 2], 1))
        else:
            tempPnts.append(Point3D(i, M_ - 1, grid[i][M_ - 1], 1))
            tempPnts.append(Point3D(i, M_, grid[i][M_], 0))
            tempPnts.append(Point3D(i, M_ + 1, grid[i][M_ + 1], 1))

        indexOfMin = 0
        minDistancePlusTangentSquare = GetSquareOfDistance(currentOptimalPoint, tempPnts[indexOfMin], dy) + GetTangentSquare(currentOptimalPoint, tempPnts[indexOfMin], dx, dy)        

        for k in range(1, len(tempPnts)):
            temp = GetSquareOfDistance(currentOptimalPoint, tempPnts[k], dy) + GetTangentSquare(currentOptimalPoint, tempPnts[k], dx, dy)
            if (temp < minDistancePlusTangentSquare):
                indexOfMin = k
                minDistancePlusTangentSquare = temp

        currentOptimalPoint = tempPnts[indexOfMin]
        optimalPath.append(currentOptimalPoint)
        tempPnts.clear()     

    # Записываем данные в текстовый файл
    fileName = "C:\\Users\\Admin\\Documents\\optimalPathPython.txt"
    with open(fileName, "w") as file:
        for point in optimalPath:
            file.write(str(round(point.N * dx, 2)) + "   " + str(round(point.M * dy, 2)) + "   " + str(point.z) + "\n")

    file.close()
    
if __name__ == "__main__":
    main()
