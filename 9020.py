# 백준 9020번 - 골드바흐의 추측
import math
from collections import deque

num = int(input())

# 소수인지 판별한다
def isPrime(nb):
    max = int(math.sqrt(nb)) + 1
    for i in range(2, max):
        if nb % i == 0:
            return 1
    return 0

# number 이하의 소수를 모두 찾는다
def findPrime(number):
    queue = deque([])
    for i in range(2, number + 1):
        if isPrime(i) == 0:
            queue.append(i)
    return queue

# 소수끼리의 합이 a이면서 차이가 가장 작은 소수 값들을 찾는다
def findMinSubPrime(a, lst):
    idx = max([i for i in range(len(lst)) if lst[i] <= a/2])
    for i in range(idx, -1, -1):
        for j in range(i, len(lst)):
            if lst[i] + lst[j] == a:
                return [lst[i], lst[j]]

# 1000 이하의 소수를 일단 모두 찾아 놓는다
lst = findPrime(10000)

for i in range(num):
    a = int(input())
    result = [0 for i in range(0,2)]

    result = findMinSubPrime(a, lst)
    print(result[0], result[1])
    
