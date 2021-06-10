import sys
import math

def merge(sub_left_list,sub_right_list):
    print('sub_left and sub_right is ', sub_left_list, sub_right_list)
    result = []
    left = 0
    right = 0
    #왼쪽배열과 오른쪽배열을 합치는 과정
    #하다가 한쪽 배열의 result append가 완료되면 탈출
    while left < len(sub_left_list) and right < len(sub_right_list) :
        if sub_left_list[left] < sub_right_list[right]:
            result.append(sub_left_list[left])
            print('result_appendend_by_sub_left ', result)
            left += 1
        else:
            result.append(sub_right_list[right])
            print('result_appended_by_sub_right ', result)
            right += 1
    #병합후에 남아있는 요소들을 병합하는 과정
    #왼쪽배열/오른쪽배열을 비교하면서 넣는 과정
    #이미 배열들은 정렬이 완료된 상태로
    #왼/오른쪽 배열 비교하면서 병합이 다 완료된 이후에
    #남아있는 배열은 이미 정렬이 되어있기때문에 그대로 넣어주면 된다.
    print('sub_left_list[left:] ', sub_left_list[left:])
    print('sub_right_list[right:] ', sub_left_list[right:])
    print('result', result)
    result += sub_left_list[left:]
    print('result_sub_left_list[left:] ', result)
    result += sub_right_list[right:]
    print('result_sub_right_list[right:] ', result)
    return result

def merge_sort(num_list):
    print('num_list is', num_list)
    if len(num_list) <= 1: #즉 재귀를 수행하면서 요소가 1이될때까지 반복
        return num_list

    mid = math.floor(len(num_list)/2)
    print('num_list[:mid]_before_sorted is ', num_list[:mid])
    print('num_list[mid:]_before_sorted is ', num_list[mid:])
    sub_left_list = merge_sort(num_list[:mid])
    print('num_list[:mid] is ', num_list[:mid])
    sub_right_list = merge_sort(num_list[mid:])
    print('num_list[mid:] is', num_list[mid:])
    return merge(sub_left_list, sub_right_list)

n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))

array = merge_sort(array)

for i in array:
    print(i)

"""
5
4
7
8
2
1
num_list is [4, 7, 8, 2, 1]
num_list[:mid]_before_sorted is  [4, 7]
num_list[mid:]_before_sorted is  [8, 2, 1]
num_list is [4, 7]
num_list[:mid]_before_sorted is  [4]
num_list[mid:]_before_sorted is  [7]
num_list is [4]
num_list[:mid] is  [4]
num_list is [7]
num_list[mid:] is [7]
sub_left and sub_right is  [4] [7]
result_appendend_by_sub_left  [4]
sub_left_list[left:]  []
sub_right_list[right:]  [4]
result [4]
result_sub_left_list[left:]  [4]
result_sub_right_list[right:]  [4, 7]
num_list[:mid] is  [4, 7]
num_list is [8, 2, 1]
num_list[:mid]_before_sorted is  [8]
num_list[mid:]_before_sorted is  [2, 1]
num_list is [8]
num_list[:mid] is  [8]
num_list is [2, 1]
num_list[:mid]_before_sorted is  [2]
num_list[mid:]_before_sorted is  [1]
num_list is [2]
num_list[:mid] is  [2]
num_list is [1]
num_list[mid:] is [1]
sub_left and sub_right is  [2] [1]
result_appended_by_sub_right  [1]
sub_left_list[left:]  [2]
sub_right_list[right:]  []
result [1]
result_sub_left_list[left:]  [1, 2]
result_sub_right_list[right:]  [1, 2]
num_list[mid:] is [2, 1]
sub_left and sub_right is  [8] [1, 2]
result_appended_by_sub_right  [1]
result_appended_by_sub_right  [1, 2]
sub_left_list[left:]  [8]
sub_right_list[right:]  []
result [1, 2]
result_sub_left_list[left:]  [1, 2, 8]
result_sub_right_list[right:]  [1, 2, 8]
num_list[mid:] is [8, 2, 1]
sub_left and sub_right is  [4, 7] [1, 2, 8]
result_appended_by_sub_right  [1]
result_appended_by_sub_right  [1, 2]
result_appendend_by_sub_left  [1, 2, 4]
result_appendend_by_sub_left  [1, 2, 4, 7]
sub_left_list[left:]  []
sub_right_list[right:]  []
result [1, 2, 4, 7]
result_sub_left_list[left:]  [1, 2, 4, 7]
result_sub_right_list[right:]  [1, 2, 4, 7, 8]
1
2
4
7
8

Process finished with exit code 0

"""
