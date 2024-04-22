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
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1), reverse=False)
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

# Ví dụ dữ liệu đầu vào
trainingSet = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
testInstance = [2, 3, 4]
k = 2

# Gọi hàm getKNeighbors và in kết quả
result = getKNeighbors(trainingSet, testInstance, k)
print(result)
