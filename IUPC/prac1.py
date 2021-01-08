# 연습문제 A - 이름궁합 테스트

# 이름 길이 입력 받기
length = input().split(' ')
len1 = int(length[0])
len2 = int(length[1])
# 이름 입력 받기(대문자로)
name = [0] * (len1 + len2)
name = input().split(' ')
name1 = name[0]
name2 = name[1]
# 알파벳의 획수를 dictionary로 정의
dic = {
    'A' : 3, 'B' : 2, 'C' : 1, 'D' : 2, 'E' : 4, 'F' : 3, 'G' : 1, 'H' : 3,
    'I' : 1, 'J' : 1, 'K' : 3, 'L' : 1, 'M' : 3, 'N' : 2, 'O' : 1, 'P' : 2,
    'Q' : 2, 'R' : 2, 'S' : 1, 'T' : 2, 'U' : 1, 'V' : 1, 'W' : 1, 'X' : 2,
    'Y' : 2, 'Z' : 1
}
# 이름을 한 글자씩 번갈아가며 적는다
if len1 - len2 == 0:
    same_len = len1
elif len1 > len2:
    same_len = len1 - abs(len1 - len2)
else:
    same_len = len2 - abs(len1 - len2)

index = 0
res = [0] * (len1 + len2)
for i in range(0, 2 * same_len, 2):
    res[i] = name1[index]
    res[i + 1] = name2[index]
    index += 1

# 번갈아가며 적다가 이름이 남을 때 남은 이름을 뒤에 마저 적는다
def make_name(len, idx_insert, idx_res, insert_name, res_name):
    for i in range(len):
        res_name[idx_res] = insert_name[idx_insert]
        idx_insert += 1
        idx_res += 1

if len1 > len2:
    dif_len = len1 - same_len
    make_name(dif_len, same_len, 2 * same_len, name1, res)
elif len1 < len2:
    dif_len = len2 - same_len
    make_name(dif_len, same_len, 2 * same_len, name2, res)

# 적은 이름을 획수(숫자)로 변경한다
size = len(res)
for i in range(size):
    res[i] = int(dic[res[i]])
# 이름 궁합 테스트를 진행한다
while size != 2:
    for i in range(size - 1):
        res[i] = (res[i] + res[i + 1]) % 10
    size -= 1
# 출력한다
ans = res[0] * 10 + res[1]
print(str(ans) + "%")