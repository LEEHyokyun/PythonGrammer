# 딕셔너리가 존재할때 key/value 가져오기

A = {
    1 : 'apple',
    2 : 'banana',
    3 : 'cone'
}

# 기본호출형태 : dictionary[key]
print(A[1])

# key/value 모두 출력
print(A.items())
# key 모두 출력
print(A.keys())
# values 모두 출력
print(A.values())

#딕셔너리 요소추가(변경) 단순형태
A[4] = 'dates'
print(A)

#딕셔너리 요소삭제 단순형태
del A[4]
print(A)

#get 함수 (get(key))
get_1 = A.get(1)
print(get_1)
get_2 = A.get('apple')
print(get_2) #None

#반복문을 통한 1차원 딕셔너리 생성
B = {}
for i in range (5):
    B[i] = i
print(B)

#공딕셔너리에서 반복문을 통한 중첩딕셔너리 값저장 불가
#C = {{}}
#for i in range(5):
    #for j in range(5):
        #C[i][j] = 1
#print(C)

