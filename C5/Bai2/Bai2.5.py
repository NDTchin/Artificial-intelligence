import numpy as np

def distance(instance1, instance2):
    instance1 = np.array(instance1)
    instance2 = np.array(instance2)
    difference = instance1 - instance2
    distance = np.linalg.norm(difference)
    return distance

# Example usage
learnset_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(distance([3, 5], [1, 1]))
print(distance(learnset_data[3], learnset_data[44]))