# 연습문제 B - 어두운 굴다리

# 굴다리의 길이 입력
length = int(input())
# 가로등의 개수 입력
cnt = int(input())
# 가로등의 위치 입력
location = [0] * cnt
location = input().split(' ')
# 맨 왼쪽, 맨 오른쪽 가로등이 길의 맨 왼쪽, 오른쪽을 비춰야 하는 길이
len_left = abs(0 - int(location[0]))
len_right = abs(length - int(location[cnt - 1]))
# 비춰야 하는 최대 길이 정의
len_max = max(len_left, len_right)
# 가로등끼리 비춰야 하는 사이 길이를 구하면서 len_max값과 비교
for i in range(cnt - 1):
    if (int(location[i + 1]) - int(location[i])) % 2 == 1:
        len_compare = (int(location[i + 1]) - int(location[i])) / 2 + 0.5
    else:
        len_compare = (int(location[i + 1]) - int(location[i])) / 2
    len_max = max(len_max, len_compare)
# 출력
print(int(len_max))