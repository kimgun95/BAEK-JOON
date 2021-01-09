# B번 - sort 마스터 배지훈의 후계자

# n, m을 입력값으로 받는다.
arr = [0] * 2
arr = input().split(' ')
n = int(arr[0])
m = int(arr[1])

# n, m의 크기만큼 리스트에 값을 입력 받는다.
a = [0] * n
d = [0] * m
for i in range(n):
    a[i] = int(input())
for i in range(m):
    d[i] = int(input())

# 리스트(a) 정렬 후 정렬된 리스트에 값들에 대한 index를 dictionary로 만든다
a.sort()
idx = 0
dic = {}
for i in a:
    if i not in dic:
        dic[i] = idx
    idx += 1

# message(d 리스트)에 등장하는 값을 dictionary에서 찾아 출력, 없다면 -1 출력
for i in d:
    if i in dic:
        print(dic[i])
    else:
        print(-1)