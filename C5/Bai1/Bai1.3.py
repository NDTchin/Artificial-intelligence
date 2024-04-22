import math
import operator

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

def getKNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x][:length], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1), reverse=False)
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

# Dữ liệu huấn luyện
trainSet = [[2, 17, '+'], [3, 11, '-'], [4, 23, '+'], [1, 12, '+'], [2, 6, '-'], 
            [6, 2, '+'], [11, 4, '-'], [2, 24, '-'], [14, 2, '-'], [9, 4, '+'], 
            [24, 23, '+'], [7, 6, '+'], [23, 4, '-'], [14, 16, '-'], [12, 3, '+']]

# Dữ liệu kiểm tra
testInstance = [3, 9]

# Số láng giềng gần nhất cần lấy
k = 5

# Gọi hàm getKNeighbors và in kết quả
neighbors = getKNeighbors(trainSet, testInstance, k)
print(neighbors)