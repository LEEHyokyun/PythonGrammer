N = 3
values = [[0] * N]* N

# range(반복횟수, 인덱스는 0부터 시작)
for i in range(N):
    values[i][0] = 1
print(values)

# range안에는 정수가 들어가야하므로 len(list) len(array)
for i in range(len(values)):
    print(i)

# list내 값들을 탐색하고 싶을때는 in list 형식
# 말 그대로 list내 value들을 모두 불러온다
# 이중배열의 경우 배열 자체가 값들이 됨
for i in values:
    print(i)

# 시작인덱스를 정할때
# 시작인덱스 ~ N-1
for i in range(1,N):
    print(i)

