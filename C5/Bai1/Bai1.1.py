import math

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

# Ví dụ dữ liệu đầu vào
instance1 = [1, 2, 3]
instance2 = [4, 5, 6]
length = len(instance1)

# Gọi hàm euclideanDistance và in kết quả
result = euclideanDistance(instance1, instance2, length)
print(result)