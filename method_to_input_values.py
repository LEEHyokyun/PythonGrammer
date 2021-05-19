import sys

# 한개의 정수를 입력받을때
a = int(sys.stdin.readline()) #자료형을 정수로 변환해야한다.
print(a)

# 한개 이상의 정수를 입력받을때
#.split()
# 스페이스바 등 특수처리을 기준으로 문자열을 나누며, 출력시에도 기본적으로 문자열 형태를 유지
#a = int(sys.stdin.readline().split())

# 이경우 int 자료형 변환이 아닌, map 함수를 통해 int 자료형으로 변환해주는 메소드가 필요
# 구분된 문자열의 개수(반환된 정수의 개수)와 저장되는 변수의 개수가 다르면 출력오류
a, b, c = map(int, sys.stdin.readline().split())
print(a, b, c)

# 임의의 개수의 정수를 입력받아 배열 혹은 리스트에 저장할때
# 배열 및 리스트 형태로 출력
array = list(map(int, sys.stdin.readline().split()))
print(array)

# 입력받은 정수를 통해 2차원 배열을 만드는 경우
# n행(줄)의 2차원 배열을 만드는 경우, for 문을 n번 반복하는 형식으로 구현
# n번 반복횟수는 입력받은 정수
array_square = []
n = int(sys.stdin.readline())
# 한 줄에 여러 개의 정수를 입력받고, 이를 n번 반복
# 한 줄마다 배열/리스트 형태로 출력되며, 이 것이 n개만큼 구현되어 2차원 배열을 형성
for i in range(n):
    array_square.append(list(map(int, sys.stdin.readline().split())))
# 출력시 N(입력받은 정수의 개수) * n(반복횟수, 행의 수)
# list가 없어지면 object 자체로 인식하여, 저장된 메모리값이 출력됨
print(array_square)

# 입력받은 문자열 자체로 배열/리스트에 저장하는 경우
n = int(sys.stdin.readline())
#입력받은 그대로 출력하면 끝에 공백문자인 \n이 출력
#이를 제거하기위해 strip() 메소드 사용
#array_string = [sys.stdin.readline()]
#strip메소드입력시 주소를 출력, strip()을 해줘야 문자열형태로 출력
array_string = [sys.stdin.readline().strip() for i in range(n)]
print(array_string) #문자열 메모리 주소 출력