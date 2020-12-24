import sys

num = int(input())
# 입력될 수 있는 최대 크기의 수인 10000으로 리스트 초기화
arr = [0] * 10001
# 입력되는 수의 index를 가진 리스트의 count를 증가
# 입력할 때 input 은 내장함수로 취급 된다고 한다.
# sys에 속하는 메소드들은 file object로 취급 되는데 사용자의 입력만을 받는 buffer를 하나 만들어 읽어 들인다고 한다
# 추가로 pypy 환경에서 쓰이지 못한다고 한다
for i in range(num):
    a = int(sys.stdin.readline())
    arr[a] += 1
# 값이 0이 아닌 리스트의 인덱스를 값의 크기만큼 반복하여 출력
for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)
