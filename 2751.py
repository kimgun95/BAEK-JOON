num = int(input())
# 입력된 num크기 만큼 리스트 초기화
arr = [0 for i in range(num)]
# 리스트에 숫자 입력
for i in range(num):
    arr[i] = int(input())
# 리스트 정렬(sort 사용)
arr.sort()
# 리스트 출력
for i in range(num):
    print(arr[i])