#!/usr/bin/env python3
from vector import Vector


# Column vector of shape n * 1
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1 * 5)
# Output
# Vector([[0.0], [5.0], [10.0], [15.0]])
# Row vector of shape 1 * n
v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = v1 * 5
print(v2)
# Output
# Vector([0.0, 5.0, 10.0, 15.0])
print(v1 / 2.0)
# Output
# Vector([0.0, 0.5, 1.0, 1.5])
print(2.0 / v1)
# Output:
# Error
print('-' * 30)

# Column vector of shape n * 1
print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
# Output
# (4,1)
print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
# Output
# [[0.0], [1.0], [2.0], [3.0]]
# Row vector of shape 1 * n
print(Vector([0.0, 1.0, 2.0, 3.0]).shape)
# Output
# (1, 4)
print(Vector([0.0, 1.0, 2.0, 3.0]).values)
# Output
# [0.0, 1.0, 2.0, 3.0]
print('-' * 30)

# Example 1:
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1.shape)
# Output:
# (4,1)
print(v1.T())
# Output:
# Vector([0.0, 1.0, 2.0, 3.0])
print(v1.T().shape)
# Output:
# (1,4)
# Example 2:
v2 = Vector([0.0, 1.0, 2.0, 3.0])
print(v2.shape)
# Output:
# (1,4)
print(v2.T())
# Output:
# Vector([[0.0], [1.0], [2.0], [3.0]])
print(v2.T().shape)
# Output:
# (4,1)
print('-' * 30)

print(v1.dot(Vector((3, 7))))
print(v1 + Vector((100, 104)))
print(v2 - Vector([6.0, 3.0, 1.0, 9.0]))
