from collections import deque

test_array_1 = deque()

test_array_1.append(2)
print(test_array_1)
test_array_1.appendleft(3)
print(test_array_1)
test_array_1.append(4)
print(test_array_1)

test_array_2 = deque()

test_array_2.append(2)
test_array_2.append(3)
test_array_2.append(4)

test_array_2.pop()
print(test_array_2)
test_array_2.popleft()
print(test_array_2)
