from itertools import permutations

num = int(input())
# 리스트 초기화 및 입력값 삽입, int 형으로 변환
arr = [0] * num
arr = input().split(' ')
for i in range(num):
    arr[i] = int(arr[i])
# 리스트의 순열 값을 생성
per = permutations(arr)
max = 0
# 순열 리스트에서 차이의 최댓값을 각각 계산하고 max를 갱신한다
for i in per:
    sum = 0
    for j in range(num - 1):
        sum += abs(i[j] - i[j + 1])
    if max < sum:
        max = sum
# 출력
print(max)